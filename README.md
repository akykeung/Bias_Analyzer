# News Article Bias Detection

The purpose of this project is to analyze and detect biases within news articles that can be found using an api from News API (https://newsapi.org/). Sentiments on Bias was detected using a machine learning pipeline developed from the huggingface community.

# Description
Media bias is ubiquitous (everywhere) and not easy to detect. It is always useful to compare several sources of information and, in doing so, it becomes clear that media coverage is never completely objective. For this project, the goal is to identify key words within different articles by identifying bias by the use of language. For example, the use of labels such as “terrorist,” “revolutionary,” or “freedom fighter” can create completely different impressions of the same person or event.

# Getting Started
## Dependencies
To run the program locally, the following libraries will be need to be imported including:
- import streamlit as st
- import requests
- import pycountry
- import spacy

## Executing program
Once libraries have been installed, the program can be run simply with the command "streamlit run app.py" or running the IDE on your local machine.

# Authors
Adrian Keung

LinkedIn: https://www.linkedin.com/in/adrian-keung/

# Version History
0.1
- Initial Release with only language bias detection. Future version to include sentiment analysis and detection of other biases including bias by image, headline and repetition.

