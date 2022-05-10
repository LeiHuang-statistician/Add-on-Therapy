# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:48:35 2022

@author: bangbang
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout='wide') 

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 200px;
        margin-left: -400px;
    }
     
    """,
    unsafe_allow_html=True,
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    
#@st.cache
def get_data():
  Tb=pd.read_csv("Table1.csv")
  return Tb 
Tb = get_data()

Tbg = Tb['Group'].unique().tolist()

Group = st.sidebar.selectbox('Select group:', Tbg)
#Group = st.sidebar.radio('Select group:',Tbg)
#Group = st.selectbox('Select group:',Tbg)


df=Tb.query("Group==@Group")


color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)','rgb(44, 160, 101)', 'rgb(255, 65, 54)']*4
tt=df['Label'].unique().tolist()
xv=np.array(df["x"].unique().tolist())
rt=np.array(df['cratio'].unique().tolist())


fig=go.Figure(
        go.Scatter(
        x=df['x'],
        y=df['y'],
        #hover_data=[text1,text2],
        text = df['Numbers']+ "<br>" + df['Percent'],
        hovertemplate = "%{text}"+"<extra></extra>",
        mode='markers',
        marker=dict(
            color=color,
            opacity=[1, 0.8, 0.6, 0.6],
            size=df['N']*rt),
        )
    )


fig.update_layout(xaxis=dict(showgrid=False),
                  yaxis=dict(showgrid=False,
                  )
)
fig.update_layout(plot_bgcolor = "white")
fig.update_xaxes( tickcolor='white')
#fig.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=14))
fig.update_yaxes(tickfont=dict(family='Rockwell', color='white', size=14))
fig.update_layout(
    xaxis = dict(
        tickmode='array', tickvals=xv, ticktext=tt,tickfont=dict(family='Rockwell', color='black', size=20)
    )
)
fig.update_layout(width=9000,height=800) #Must have to show all

with st.container():
      st.plotly_chart(fig,use_container_width=True)
