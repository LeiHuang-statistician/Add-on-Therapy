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
        width: 400px;
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
 Tb=pd.read_csv("Table2.csv",encoding="latin-1")
 return Tb 
Tb = get_data()

Tbg = Tb['Group'].unique().tolist()

#Group = st.sidebar.selectbox('Select group:', Tbg)
Group = st.sidebar.radio('Select group:',Tbg)
#Group = st.selectbox('Select group:',Tbg)
color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)','rgb(44, 160, 101)', 'rgb(255, 65, 54)']

df=Tb.query("Group==@Group")


color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)','rgb(44, 160, 101)', 'rgb(255, 65, 54)']

df['P'] = df['P'].astype(float).map('{:,.1f}'.format)

df["x"] = df["x"].astype(str)
tt=df['Label'].unique().tolist()
name=df['LDL cholesterol, mg/dL'].unique().tolist()
anoa = (df["x"]).sort_values().unique()
dft=df[['x','T']].drop_duplicates()


y0 = df.loc[df['LDL cholesterol, mg/dL']==name[0],['N','P']]
y1 = df.loc[df['LDL cholesterol, mg/dL']==name[1],['N','P']]
y2 = df.loc[df['LDL cholesterol, mg/dL']==name[2],['N','P']]
y3 = df.loc[df['LDL cholesterol, mg/dL']==name[3],['N','P']]


trace0 = go.Bar(
x= tt,
y= y0['N'],
marker= dict (color =color[0] ),
name = name[0],
text=y0['P']+"%",
insidetextanchor="middle",
textfont_color='white',
)


trace1 = go.Bar(
x=tt,
y= y1['N'],
marker= dict (color =color[1] ),
name = name[1],
text=y1['P']+"%",
insidetextanchor="middle",
textfont_color='white',
)

trace2 = go.Bar(
x=tt,
y= y2['N'],
marker= dict (color =color[2] ),
name = name[2],
text=y2['P']+"%",
insidetextanchor="middle",
textfont_color='white',
)


trace3 = go.Bar(
x=tt,
y= y3['N'],
marker= dict (color =color[3] ),
name = name[3],
text=y3['P']+"%",
insidetextanchor="middle",
textfont_color='white',
)


layout = go.Layout(
title= 'LDL-cholesterol distribution' ,
barmode = 'stack',

)
data = [trace0,trace1,trace2, trace3]
fig = go.Figure(data=data, layout=layout)
# Hide grid lines
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)




fig.update_layout(plot_bgcolor = "white")
fig.update_xaxes( tickcolor='white')
#fig.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=14))
fig.update_yaxes(tickfont=dict(family='Rockwell', color='white', size=14))
fig.update_yaxes(title='y', visible=False, showticklabels=False)
fig.update_xaxes(title=' ', visible=True, showticklabels=True)
fig.update_layout(
    annotations=[
        {"x": (anoa == x).argmax(), "y": total + (dft["T"].max()/13), "text": f"{total} Millions", "showarrow": False}
        for x, total in dft.values
    ], font_size=20, title_x=0.5
)

#fig.update_layout(uniformtext_minsize=16, uniformtext_mode='hide')

#fig.update_layout(margin=dict(l=5, r=5, t=150, b=100)) 
fig.update_layout(width=1500,height=800) #Must have to show all


with st.container():
     st.plotly_chart(fig,use_container_width=True)
