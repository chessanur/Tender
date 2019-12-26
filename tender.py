## IMPORT LIBRARY ##
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import metrics
import pickle

def search_weights(search_keys):  
    search_query_weights = search_keys.lower()
    tfidf_weights_matrix = tfidfVectorizer.fit_transform(raw_data_1['preprocessing'])
    search_query_weights = tfidfVectorizer.transform([search_keys])
    
    return search_query_weights, tfidf_weights_matrix

def cos_similarity(search_query_weights, tfidf_weights_matrix):

    cosine_distance = cosine_similarity(search_query_weights, tfidf_weights_matrix)
    similarity_list = cosine_distance[0]

    return similarity_list


raw_data_1 = pd.read_csv("./data.csv")
search = st.text_input('Search:')
max_data = st.number_input('max data: ')

tfidfVectorizer = TfidfVectorizer()

weights_search, tfidf_weights = search_weights(search)

similarity = cos_similarity(weights_search, tfidf_weights)
df = pd.DataFrame({'res':similarity})
df = df.sort_values(by=['res'],ascending=False)

if (len(search) != 0):
    index= []
    for i in df.index: 
        index.append(i)

    count=1
    for i in index:
        if count <= max_data: 
            if st.button(raw_data_1['nama_tender'].loc[i],key = count):
                """## Analysis"""
                analysis_data = raw_data_1.loc[i]
                analysis_data
            st.write("HPS: ", raw_data_1['hps'].loc[i])
            st.write("Instansi: ", raw_data_1['instansi'].loc[i])
            st.write("Status: ", raw_data_1['status_tender'].loc[i])
            st.write("\n")
            count=count+1

                
