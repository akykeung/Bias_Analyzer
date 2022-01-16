#Import all dependencies and libraries
import streamlit as st
import requests
import pycountry
import spacy
from api import apiKEY

#Create title of web page
st.title("News key Words Bias Detector")

#Reorganize the selections
col1, col2 = st.columns([4,5])
with col1:
    #Enter Country
    st.text_input("Enter Country Name") 

with col2:
    #Selection of categories
    st.radio('Choose what type of news you are interested in:', ('Technology', 'Business', 'Politics', 'Sports'))

#Loading with progress
with st.progress("Please wait for the text to be analyzed..."):
    nlp = spacy.load("en_pipeline")

#Text entry for user input
input = st.text_area(label = "Enter your text to get biased words")

# Create a doc object

doc = nlp(input)

# HTML -> markdown code to display code

output_html = spacy.displacy.render(doc, style='ent', jupyter=False, options = {"colors": {'Possible bias detected':'#ffd966'})

# Render the html code as a markdown with html enabled

st.markdown(output_html,    unsafe_allow_html=False)