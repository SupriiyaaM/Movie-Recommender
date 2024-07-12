'''
without markdown
import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f3cd847b635146c101bfc6fca8cf753b&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', None)
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    else:
        return None
    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names,recommended_movie_posters

st.header('Movie Recommender System')

# Define the absolute paths to the pickle files
movies_file_path = 'C:/Users/SUPRIYA MISHRA/OneDrive/Desktop/ML-MovieRec/movies_dict1.pkl'
similarity_file_path = 'C:/Users/SUPRIYA MISHRA/OneDrive/Desktop/ML-MovieRec/similarity1.pkl'

# Load the pickled files
try:
    with open(movies_file_path, 'rb') as f:
        movies_dict = pickle.load(f)
        movies = pd.DataFrame.from_dict(movies_dict)
    with open(similarity_file_path, 'rb') as f:
        similarity = pickle.load(f)
except Exception as e:
    st.error(f"Error loading pickle files: {e}")

# Proceed only if the DataFrame is valid
if isinstance(movies, pd.DataFrame) and 'title' in movies.columns:
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )
                
    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5,col6, col7, col8, col9, col10 = st.columns(10)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
        with col6:
            st.text(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
        with col7:
            st.text(recommended_movie_names[6])
            st.image(recommended_movie_posters[6])
        with col8:
            st.text(recommended_movie_names[7])
            st.image(recommended_movie_posters[7])
        with col9:
            st.text(recommended_movie_names[8])
            st.image(recommended_movie_posters[8])
        with col10:
            st.text(recommended_movie_names[9])
            st.image(recommended_movie_posters[9])
else:
    st.error("Movies DataFrame is not valid or 'title' column is missing.")
'''


import pickle
import streamlit as st
import requests
import pandas as pd

# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f3cd847b635146c101bfc6fca8cf753b&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path', None)
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error("ERROR : Unable To Fetch Data. Connect to VPN to get valid results or try again later.")
        st.stop()

    
# Function to recommend movies based on selected movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_movie_posters

# Setting Streamlit app title and page configuration
st.set_page_config(
    page_title="Movie Mirror: Find Movies similar to your favourites!",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Customizing the style of the UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #D1CFE2;
    }
    .stHeader {
        background-color: #004d40;
        color: white;
        font-size: 36px;
        padding: 1rem;
        text-align: center;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background-color: #388e3c !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header for the Movie Recommender System
st.markdown("<h1 class='stHeader'>Movie Mirror: find movies similar to your favourites!</h1>", unsafe_allow_html=True)

# Define the absolute paths to the pickle files
movies_file_path = 'C:/Users/SUPRIYA MISHRA/OneDrive/Desktop/ML-MovieRec/movies_dict1.pkl'
similarity_file_path = 'C:/Users/SUPRIYA MISHRA/OneDrive/Desktop/ML-MovieRec/similarity1.pkl'

# Load the pickled files
try:
    with open(movies_file_path, 'rb') as f:
        movies_dict = pickle.load(f)
        movies = pd.DataFrame.from_dict(movies_dict)
    with open(similarity_file_path, 'rb') as f:
        similarity = pickle.load(f)
except Exception as e:
    st.error(f"Error loading pickle files: {e}")

# Proceed only if the DataFrame is valid
if isinstance(movies, pd.DataFrame) and 'title' in movies.columns:
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
    "**Type or select a movie from the dropdown below**",
    movie_list
)

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        st.subheader("Recommended Movies")
        cols = st.columns(5)
        for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            with col:
                st.text(name)
                st.image(poster)
else:
    st.error("Movies DataFrame is not valid or 'title' column is missing.")
    
