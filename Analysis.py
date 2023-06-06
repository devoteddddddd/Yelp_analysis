import pandas as pd
import streamlit as st
from PIL import Image
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


st.set_page_config(page_title="Analysis system for merchant")

image1 = Image.open('./f1.png')
image2 = Image.open('./f2.png')
image3 = Image.open('./f3.png')
image4 = Image.open('./f4.png')
image5 = Image.open('./f5.png')
image6 = Image.open('./f6.png')
image7 = Image.open('./f7.png')
image8 = Image.open('./f8.png')
image9 = Image.open('./f9.png')
image10 = Image.open('./f10.png')
image11 = Image.open('./f11.png')
image12 = Image.open('./f12.png')

df = pd.read_csv('./Health_business.csv')
lats = df['latitude'].tolist()
lons = df['longitude'].tolist()
locations = list(zip(lats, lons))
map1 = folium.Map(location=[37.0902, -95.7129], tiles='OpenStreetMap', zoom_start=5)
FastMarkerCluster(data=locations).add_to(map1)

st.write("# Hi, Dear merchant👋")

st.markdown(
    """
    ### We provide our visualization results here for your reference! They are mainly about Health and Medical businesses in Yelp dataset.
    """
)

st.image(image1, caption='The top 15 commonly used attributes of Health and Medical businesses', use_column_width=True,  output_format='PNG')
st.image(image2, caption='The top 50 commonly used categories of Health and Medical businesses', use_column_width=True,  output_format='PNG')
st.image(image3, caption='The x-axis is the star rating, and the y-axis is the number of businesses possessing that rating', use_column_width=True,  output_format='PNG')
st.image(image4, caption='Distribution of checkin count', use_column_width=True,  output_format='PNG')
st.image(image5, caption='Distribution of review count', use_column_width=True,  output_format='PNG')
st.image(image6, caption='Percentages of businesses at regional level', use_column_width=True,  output_format='PNG')
st.image(image7, caption='Average rating of each category', use_column_width=True,  output_format='PNG')
st.image(image8, caption='Features related to star rating', use_column_width=True,  output_format='PNG')
st.image(image9, caption='Confusion matrix about features related to star rating', use_column_width=True,  output_format='PNG')
st.image(image10, caption='Word cloud graph for all reviews of all Health and Medical businesses', use_column_width=True,  output_format='PNG')
st.image(image11, caption='Word cloud graph for positive reviews of all Health and Medical businesses', use_column_width=True,  output_format='PNG')
st.image(image12, caption='Word cloud graph for negative reviews of all Health and Medical businesses', use_column_width=True,  output_format='PNG')
st.markdown(
    """
    Here is the location distribution of all the Health and Medical businesses.
    """
)
st_data = st_folium(map1, width=725)