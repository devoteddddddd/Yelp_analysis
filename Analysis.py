
import streamlit as st
from PIL import Image



st.set_page_config(page_title="Analysis system for merchant")



image1 = Image.open('./f1.png')



st.write("# Hi, Dear merchant👋")

st.markdown(
    """
    We provide our visualization results here for your reference! They are mainly about Health and Medical businesses in Yelp dataset.
    """
)

st.image(image1, caption='The top 15 commonly used attributes of Health and Medical businesses', use_column_width=True,  format='PNG')
