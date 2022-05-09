
import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title(':bar_chart:Add-On Therapy Study')

    st.markdown(""" <style> .font {
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Welcome to explore the data</p>', unsafe_allow_html=True)

    

    st.write('Navigate to `Table` page to visualize the data')
