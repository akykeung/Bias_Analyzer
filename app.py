#Import all dependencies and libraries
import streamlit as st
import requests
import pycountry
import spacy
#from api import apiKEY

apiKEY = '4edfd5e480fb42098234171216e701a3'

#Create title of web page
st.title("News key Words Bias Detector")

#Reorganize the selections
col1, col2 = st.columns([4,5])
with col1:
    #Enter Country
    try:
        user = st.text_input("Enter Country Name") 

    except:
        st.write('Please enter the full name of the country, ie. United States')

with col2:
    #Selection of categories
    category = st.radio('Choose what type of news you are interested in:', ('Technology', 'Business', 'Politics', 'Sports'))
    btn = st.button('Enter')

if btn:
    country = pycountry.countries.get(name=user).alpha_2
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={apiKEY}"
    r = requests.get(url)
    
    #JSON File creation
    r = r.json()
    articles = r['articles']

    # Create a doc object
    nlp = spacy.load('en_pipeline')


    for article in articles:
        st.header(article['title'])
        st.write("Published at: ", article['publishedAt'])
        #Author
        if article['author']:
            st.write('Written by: ', article['author'])
        else:
            st.write('Error retrieving author')
        st.write('Article Link: ',article['url'])
        st.markdown(f"<h1 style ='background-color:gray; text-align: center; border-radius:20px;'> {article['source']['name']} </h1>", unsafe_allow_html=True)
        st.markdown(spacy.displacy.render(nlp(article['description']), style = 'ent', options = {"colors": {'Possible bias detected':'#FF0000'}}),    unsafe_allow_html=True)
        if article['urlToImage']:    
            st.image(article['urlToImage'])
        else:
            st.markdown("<h3 style=text-align: center;'> Error retrieving Image...</h3>", unsafe_allow_html=True)
