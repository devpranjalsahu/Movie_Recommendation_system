import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return movie_list[movie_list.index == index]["title"].values[0]
def get_index_from_title(title):
	return movie_list[movie_list.title == title]["index"].values[0]

movie_list=pd.read_csv("movie_dataset.csv")

features=['keywords','cast','genres','director']

for feature in features:
    movie_list[feature]=movie_list[feature].fillna('')

def combine_features(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
movie_list['combined_features']=movie_list.apply(combine_features,axis=1)

cv=CountVectorizer()
count_matrix=cv.fit_transform(movie_list['combined_features'])

cosine_sim=cosine_similarity(count_matrix)

movie_user_likes = input("Enter favorite Movie: ")
movie_user_likes=movie_user_likes.title()
num=int(input("Enter number of movies you want: "))
try:
    movie_index=get_index_from_title(movie_user_likes)
    similar_movies=list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
    i,j=0,0
    for movie in sorted_similar_movies:
        if j==0:
            print("Your Movie: ",movie_user_likes)
            j=1
            print("Recommended Movies: ")
        else:
            print(get_title_from_index(movie[0]))
            i=i+1
            if i>num:
                break
except:
    print("Sorry we cannot recommend you movie for movie :",movie_user_likes)