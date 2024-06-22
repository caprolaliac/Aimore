# pip install -r requirements.txt
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
import requests

# Function to get movie recommendations from the phi3 model using Ollama
def get_movie_reccs(genre, year_range, mood, custom_text):
    # LLM {using phi3 from Ollama}
    llm = ChatOllama(model='phi3')
    
    # Prompt template
    template = """
    You are a knowledgeable movie recommendation system. Suggest a good movie based on the following criteria:
    Genre: {genre}
    Year Range: {year_range}
    Mood: {mood}
    Additional Information: {custom_text}

    Please provide a recommendation in the following format:

    Movie Title (Year)
    Synopsis: Brief summary of the movie's plot.
    Key Points:
    * Director: Name of the director
    * Starring: Main cast members
    * Genre: Movie genres
    * Accolades: Any notable awards or recognition

    Conclude with a brief explanation of why this movie is a good fit for the given criteria.
    """
    prompt = PromptTemplate(input_variables=["genre", "year_range", "mood", "custom_text"], template=template)
    chain = LLMChain(prompt=prompt, llm=llm, output_parser=StrOutputParser())
    
    # Generating response
    response = chain.run({"genre": genre, "year_range": year_range, "mood": mood, "custom_text": custom_text})
    
    # Extracting title from movie for searching movie with tmdb api
    lines = response.split('\n')
    movie_title = lines[0].strip()
    
    return movie_title, response

# Function to fetch movie metadata from TMDb
def fetch_movie_metadata(movie_title, api_key):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(search_url)
    data = response.json()
    if data['results']:
        movie_data = data['results'][0]
        return movie_data
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="Movie Recommendation System",
                   page_icon=';)',
                   layout='centered',
                   initial_sidebar_state='expanded')

st.header("AI Movie Recommendation System")

genre = st.multiselect("Select genres", 
                       ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
                        'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 
                        'Horror', 'Indie', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 
                        'Thriller', 'War', 'Western'])

year_range = st.multiselect('Select year ranges',
                            ['before 1950s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])

mood = st.multiselect('Select moods',
                      ['Uplifting', 'Thoughtful', 'Exciting', 'Relaxing', 'Intense', 'Funny',
                       'Emotional', 'Inspirational', 'Nostalgic', 'Romantic', 'Suspenseful', 
                       'Heartwarming', 'Melancholic', 'Whimsical', 'Dark', 'Quirky', 
                       'Thought-provoking', 'Feel-good', 'Gritty', 'Epic'])

custom_text = st.text_area("Any additional info you'd like to provide?")

submit = st.button("Get Recommendation")

tmdb_api_key = 'Your_Api_key' #Enter your api key from tmdb

if submit:
    if genre and year_range and mood:
        genre_str = ", ".join(genre)
        year_range_str = ", ".join(year_range)
        mood_str = ", ".join(mood)
        
        movie_title, recommendation_response = get_movie_reccs(genre_str, year_range_str, mood_str, custom_text)
        
        st.subheader("Movie Recommendation:")
        st.write(recommendation_response)
        
        #if user clicks on this button it redirects to the tmdb page of the film {not working}
        if st.button("Get More Details from TMDb"):
            movie_metadata = fetch_movie_metadata(movie_title, tmdb_api_key)
            
            if movie_metadata:
                tmdb_url = f"https://www.themoviedb.org/movie/{movie_metadata['id']}"
                st.markdown(f'<a href="{tmdb_url}" target="_blank">View on TMDb</a>', unsafe_allow_html=True)
            else:
                st.write("Sorry, no metadata found for the recommended movie.")
    else:
        st.write("Please select at least one option for genre, year range, and mood.")
