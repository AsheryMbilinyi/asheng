import json
import condorcet
import pandas as pd
import numpy as np

from scipy import stats
from ast import literal_eval
from django.shortcuts import render
from .forms import UserInputsForm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

credits_df = pd.read_csv("/Users/hekima/MovieRecommendation/nyx/asheng/recommendations/tmdb_5000_credits.csv")
movies_df = pd.read_csv("/Users/hekima/MovieRecommendation/nyx/asheng/recommendations/tmdb_5000_movies.csv")

#megging both dataframes
credits_df.columns = ['id','title','cast','crew']
movies_df = movies_df.merge(credits_df, on="id", suffixes=('_x','')).drop('title_x', axis=1)

features = ["cast", "crew", "keywords", "genres"]
for feature in features:
    movies_df[feature] = movies_df[feature].apply(literal_eval)


# get the director's name
def get_director(x):
    for i in x:
        if i["job"] == "Director":
            return i["name"]
    return np.nan


# return top three elements
def get_list(x):
    if isinstance(x, list):
        names = [i["name"] for i in x]

        if len(names) > 3:
            names = names[:3]

        return names

    return []

movies_df["director"] = movies_df["crew"].apply(get_director)

features = ["cast", "keywords", "genres"]
for feature in features:
    movies_df[feature] = movies_df[feature].apply(get_list)


#The next step would be to convert the above feature instances into lowercase and
#remove all the spaces between them.
def clean_data(row):
    if isinstance(row, list):
        return [str.lower(i.replace(" ", "")) for i in row]
    else:
        if isinstance(row, str):
            return str.lower(row.replace(" ", ""))
        else:
            return ""


features = ['cast', 'keywords', 'director', 'genres']
for feature in features:
    movies_df[feature] = movies_df[feature].apply(clean_data)

#Now, let’s create a “soup” containing all of the metadata information extracted to
#input into the vectorizer.
def create_soup(features):
    return ' '.join(features['keywords']) + ' ' + ' '.join(features['cast']) + ' ' + features['director'] + ' ' + ' '.join(features['genres'])

movies_df["soup"] = movies_df.apply(create_soup, axis=1)


#vectorizing the "soup" of the each movie
count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(movies_df["soup"])
#print(count_matrix.shape)
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
#print(cosine_sim2.shape)
movies_df = movies_df.reset_index()
indices = pd.Series(movies_df.index, index=movies_df['title'])

indices = pd.Series(movies_df.index, index=movies_df["title"]).drop_duplicates()


# this is recommondation is based on movie contents (content based)
def get_recommendations(title, cosine_sim):
    idx = indices[title]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    #print(similarity_scores)
    similarity_scores= similarity_scores[1:11]
    # (a, b) where a is id of movie, b is similarity_scores

    movies_indices = [ind[0] for ind in similarity_scores]
    movies = movies_df["title"].iloc[movies_indices]
    return movies


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserInputsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Get the current instance object to display in the template
            img_obj = form.instance
            user_input_movie = img_obj.title
            user_input_genre = img_obj.genre

            # get a ranked list based on contents
            recomended_movies_contents = get_recommendations(user_input_movie, cosine_sim2).tolist()
            # print(recomended_movies_contents)
            # get a ranked list for the same movie based on emotions
            f = open('/Users/hekima/MovieRecommendation/nyx/asheng/recommendations/similar_movies_emotionally_withtitles.json')
            similar_movies = json.load(f)
            recomended_movies_based_on_emotion = similar_movies[user_input_movie]

            # check spearman ranking correlation between two ranks
            emotions = []
            content = []
            votes = [{}, {}]  # combine both ranking for condorcet calculations
            for count, element in enumerate(recomended_movies_based_on_emotion):
                emotions.append(count + 1)
                votes[0][element] = count + 1
                try:
                    index = recomended_movies_contents.index(element)
                    content.append(index + 1)
                    votes[1][element] = index + 1
                except ValueError:  # catch exception if the element is not in the second list
                    content.append(0)

            spearman_correlation = stats.spearmanr(emotions, content)
            # if there is slight correlation combine two ranking using condorcet method
            final_recommendations=[]
            if spearman_correlation[0] in np.arange(0, 1, 0.1):
                evaluator = condorcet.CondorcetEvaluator(candidates=recomended_movies_based_on_emotion, votes=votes)
                winners, rest_of_table = evaluator.get_n_winners(4)
                final_recommendations=winners
            else:
                final_recommendations=recomended_movies_based_on_emotion



            #print(user_input_genre)

            context = {'form':form,
                       'img_obj': img_obj,
                       'user_input_movie':user_input_movie,
                       'final_recommendations': recomended_movies_contents,
                       #'final_recommendations': recomended_movies_based_on_emotion,

                       #'final_recommendations':final_recommendations
                       }

            return render(request, 'recommendations/index.html',context)

    else:
        form = UserInputsForm()

    return render(request,'recommendations/index.html',{'form':form})
