import streamlit as st
import pickle
import pandas as pd
import requests

def fecthPoster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2f203ad7a297788020cff0a7d2816d61".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']


def recommend(movie):
    recommended_movie_list=[]
    recommended_movies_posters=[]
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].movie_id
        recommended_movie_list.append(movies.iloc[i[0]].title)
        # fetch posters from api
        recommended_movies_posters.append(fecthPoster(movies_id))
    return recommended_movie_list,recommended_movies_posters

movies_dict=pickle.load(open("movies_dict.pkl",'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pkl",'rb'))

st.title("Movie Recommender system")

selected_movie_name=st.selectbox('Choose your movie',(movies['title'].values))

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0],width=200)
    with col2:
        st.text(names[1])
        st.image(posters[1],width=200)
    
    with col3:
        st.text(names[2])
        st.image(posters[2],width=200)

    col4,col5=st.columns(2)

    with col4:
        st.text(names[3])
        st.image(posters[3],width=200)

    with col5:
        st.text(names[4])
        st.image(posters[4],width=200)
