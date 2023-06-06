import pandas as pd
import streamlit as st
from PIL import Image
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


st.set_page_config(page_title="Analysis system for merchant")

image1 = Image.open('./f1.png')
image2 = Image.open('./f2.png')
df = pd.read_csv('./Health_business.csv')
lats = df['latitude'].tolist()
lons = df['longitude'].tolist()
locations = list(zip(lats, lons))
map1 = folium.Map(location=[37.0902, -95.7129], tiles='OpenStreetMap', zoom_start=5)
FastMarkerCluster(data=locations).add_to(map1)

st.write("# Hi, Dear merchant👋")

st.markdown(
    """
    We provide our visualization results here for your reference! They are mainly about Health and Medical businesses in Yelp dataset.
    """
)

st.image(image1, caption='The top 15 commonly used attributes of Health and Medical businesses', use_column_width=True,  output_format='PNG')
st.image(image2, caption='The top 50 commonly used categories of Health and Medical businesses', use_column_width=True,  output_format='PNG')
st_data = st_folium(map1)