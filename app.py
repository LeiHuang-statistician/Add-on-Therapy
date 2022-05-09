# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:52:38 2022

@author: bangbang
"""

import streamlit as st
from multiapp import MultiApp
from apps import home, page1,page2 # import your app modules here


app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Table1", page1.app)
app.add_app("Table2", page2.app)


# The main app
app.run()