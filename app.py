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
    user = st.text_input("Enter Country Name") 

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
        st.write(article['source']['name'])
        st.markdown(spacy.displacy.render(nlp(article['description']), style = 'ent', options = {"colors": {'Possible bias detected':'#ffd966'}}),    unsafe_allow_html=True)
        st.image(article['urlToImage'])



    # HTML -> markdown code to display code

    #output_html = spacy.displacy.render(doc, style='ent', jupyter=False, options = {"colors": {'Possible bias detected':'#ffd966'}})

    # Render the html code as a markdown with html enabled

    #st.markdown(output_html,    unsafe_allow_html=False)