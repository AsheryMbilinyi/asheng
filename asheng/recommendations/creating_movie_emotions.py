import csv
import json
import numpy as np


movies = {}
emotion_vectors = []
with open('tmdb_5000_credits.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for count,row in enumerate(reader):
        movie_id = (row['movie_id'])
        movie_title = (row['title'])
        #print(movie_title)
        movies[movie_id]=movie_title
        # if count == 10:
        #     break
        emotion_vectors = np.random.rand(100)
        np.save(movie_id,emotion_vectors)

#save movies id and their title in json file
with open('movies.json','w') as fp:
    json.dump(movies,fp)

# print(emotion_vectors)
# print(emotion_vectors.shape)


