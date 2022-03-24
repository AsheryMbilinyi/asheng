import json
import numpy as np
from pathlib import Path
from collections import defaultdict

# Defining a dict
similar_movies = defaultdict(list)
#read movies id-title file
f = open('movies.json')
movies = json.load(f)

movie_id = []
movie_emotions=[]


#loading the emotions_vectors for each movie
for emotions in Path("/Users/hekima/MovieRecommendation/MovieEmotions").glob("*.npy"):
    movie_emotions.append(np.load(emotions))
    movie_id.append(emotions.stem)
    #movie_id.append()

#finding similar movies (shortest L2 distance) for each movie_id based on emotions
for i in range(len(movie_emotions)):
    corrensponding_movie_id = movie_id[i]
    the_movie = movies[corrensponding_movie_id]
    #similar_movies[movie_id]
    query =  movie_emotions[i]
    dists = np.linalg.norm(movie_emotions-query, axis=1) #L2 distance
    ids = np.argsort(dists)[:10]  # Top 10 results
    for id in ids:
        similar_movies[the_movie].append(movies[movie_id[id]])  #put similar movies in defaultdict
        #similar_movies[corrensponding_movie_id].append(movie_id[id]) #put similar movies in defaultdict

##make a hard_copy file of each movie with its similar movies emotionally
with open('similar_movies_emotionally_withtitles.json','w') as fp:
    json.dump(similar_movies,fp)






