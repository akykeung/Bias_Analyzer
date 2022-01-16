#Import all dependencies and libraries
import streamlit as st
import spacy

#Create title of web page
st.title("Key Words Bias Detector")

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