# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:12:08 2022

@author: bangbang
"""


import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
st.set_page_config(layout='wide')



st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 350px;
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
 Tb=pd.read_csv("Table2.csv")
 return Tb 
Tb = get_data()

Tbg = Tb['Group'].unique().tolist()

#Group = st.sidebar.selectbox('Select group:', Tbg)
Group = st.sidebar.radio('Select group:',Tbg)
#Group = st.selectbox('Select group:',Tbg)


df=Tb.query("Group==@Group")


tt=df['Label'].unique().tolist()
xv=np.array(df["x"].unique().tolist())


#fig = px.bar(df, x="Label", y="N", color="Category", title="Long-Form Input")
fig = px.bar(df, x="x", y="N", color="LDL cholesterol, mg/dL",text='Percent',custom_data=['LDL cholesterol, mg/dL','Percent'])
fig.update_traces(hovertemplate='%{customdata[0]}<br>%{customdata[1]}<extra></extra>')

fig.update_layout(
    xaxis = dict(
        tickmode='array', tickvals=xv, ticktext=tt,tickfont=dict(family='Rockwell', color='black', size=20)
    )
)

fig.update_layout(plot_bgcolor = "white")
fig.update_xaxes( tickcolor='white')
#fig.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=14))
fig.update_yaxes(tickfont=dict(family='Rockwell', color='white', size=14))
fig.update_layout(plot_bgcolor = "white")
fig.update_yaxes(title='y', visible=False, showticklabels=False)
fig.update_xaxes(title=' ', visible=True, showticklabels=True)

fig.update_layout(width=9000,height=800) #Must have to show all


with st.container():
     st.plotly_chart(fig,use_container_width=True)

        
  
