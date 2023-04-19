import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
st.set_page_config(
    page_title="Project Web Scraping",
    page_icon=":tada:",
    layout="wide",
)
#st.title("Evolution of World Happiness")
#st.write("In this project we want to analyze the **World Happiness** in the last years and try to understand what contribute to the results")
st.sidebar.header("World Happiness Analysis")
#st.sidebar.slider('Select the Year', 2015, 2021)
#################
#dataset will come here:
df2019 = pd.read_csv("https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2019.csv")
df2018 = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2018.csv')
#################
choice = st.sidebar.radio("Select the Topic", ('Overall Happiness','Happiness by Region','Wealth Potential','Social Support','Correlations'))
if choice == 'Overall Happiness':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Happiness by Region':
    st.header("World Happiness Analysis 2019")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Wealth Potential':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Social Support':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Correlations':
    st.header("World Happiness Analysis 2018")
    st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("here column 1")
            #some graphs or tables
        with col2:
            st.write("here column 2")
            #some graphs or tables
    pages = {
        "Plot1": page_plot1,    #names will change, don't worry :)
        "Plot2": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()