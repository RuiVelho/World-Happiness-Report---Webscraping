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
    st.header("World Happiness Analysis")
    st.subheader("The 10 happiest countries in 2018 and 2019")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            sorted_df2019 = df2019.sort_values(by='Score', ascending=False)
            top_10_happiest2019 = sorted_df2019.head(10)
            viz10=sns.barplot(x='Country or region', y='Score', data=top_10_happiest2019, palette="ch:s=.25,rot=-.25")
            plt.ylim(6,8)
            plt.title('Top 10 Happiest Countries in the World in 2019')
            plt.xlabel('')
            plt.ylabel('Happiness Score')
            plt.xticks(rotation=45)
            st.pyplot(viz10.figure)
        with col2:
            st.write("")
            sorted_df2018 = df2018.sort_values(by='Score', ascending=False)
            top_10_happiest2018 = sorted_df2018.head(10)
            viz11=sns.barplot(x='Country or region', y='Score', data=top_10_happiest2018, palette="ch:s=.25,rot=-.25")
            plt.ylim(6,8)
            plt.title('Top 10 Happiest Countries in the World in 2018')
            plt.xlabel('')
            plt.ylabel('Happiness Score')
            plt.xticks(rotation=45)
            st.pyplot(viz11.figure)
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            sorted_df2019 = df2019.sort_values(by='Score', ascending=True)
            top_10_unhappiest2019 = sorted_df2019.head(10)
            viz12=sns.barplot(x='Country or region', y='Score', data=top_10_unhappiest2019, palette="flare")
            plt.ylim(2,4)
            plt.title('Top 10 Unhappiest Countries in the World of 2019')
            plt.xlabel('')
            plt.ylabel('Happiness Score')
            plt.xticks(rotation=45)
            st.pyplot(viz12.figure)
        with col2:
            st.write("")
            sorted_df2018 = df2018.sort_values(by='Score', ascending=True)
            top_10_unhappiest2018 = sorted_df2018.head(10)
            viz13=sns.barplot(x='Country or region', y='Score', data=top_10_unhappiest2018, palette="flare")
            plt.ylim(2,4)
            plt.title('Top 10 Unhappiest Countries in the World in 2018')
            plt.xlabel('')
            plt.ylabel('Happiness Score')
            plt.xticks(rotation=45)
            st.pyplot(viz13.figure)
    pages = {
        "Happiness Data": page_plot1,    #names will change, don't worry :)
        "Unhapiness Data": page_plot2     #names will change, don't worry :)
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
    st.header("Wealth Potential Analysis")
    st.subheader("How many resources can a country spend in order to improve it´s citizens life?")
    def page_plot1():
        col1, col2, = st.columns(2)
        with col1:
            st.write("How happy are the citizens in a particular country")
            sorted_df2019 = df2019.sort_values(by='Score', ascending=False)
            top_10_happiest2019 = sorted_df2019.head(10)
            viz10=sns.barplot(x='Country or region', y='Score', data=top_10_happiest2019, palette="ch:s=.25,rot=-.25")
            plt.ylim(6,8)
            plt.title('Top 10 Happiest Countries in the World in 2019')
            plt.xlabel('')
            plt.ylabel('Happiness Score')
            plt.xticks(rotation=45)
            st.pyplot(viz10.figure)
        with col2:
            st.write("... and how much could a country contribute to actually improve it?")
            sorted_df2019 = df2019.sort_values(by='GDP per capita', ascending=False)
            top_10_GDP = sorted_df2019.head(10)
            viz14=sns.barplot(x='Country or region', y='GDP per capita', data=top_10_GDP, palette="ch:s=.25,rot=-.25")
            plt.ylim(6,8)
            plt.title('Top 10 Countries with highest Wealth Potential in 2019')
            plt.xlabel('')
            plt.ylabel('Wealth Potential')
            plt.xticks(rotation=45)
            st.pyplot(viz14.figure)   
        st.write("By observing the 2019 results it is possible to observe that some of the wealthiest countries do not necessarily possess the happiest citizens, altough its capacity to do so should not be understimated")
    def page_plot2():
        col1, col2 = st.columns(2)
        with col1:
            st.write("")
            sorted_df2019 = df2019.sort_values(by='Score', ascending=False)
            top_10_happiest2019 = sorted_df2019.head(10)
            viz10=sns.barplot(x='Country or region', y='Score', data=top_10_happiest2019, palette="ch:s=.25,rot=-.25")
            plt.ylim(6,8)
            plt.title('Top 10 Happiest Countries in the World in 2019')
            plt.xlabel('')
            plt.ylabel('Happiness Score')
            plt.xticks(rotation=45)
            st.pyplot(viz10.figure)
        with col2:
            st.write("")
            Table_Economic_Freedom = pd.read_csv("https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/Table_Economic_Freedom.csv")
            top_10 = Table_Economic_Freedom.head(10)
            plt.ylim(70,85)
            viz20=sns.barplot(x='Countries', y='Economic freedom, overall index, 2022', data=top_10, palette="ch:s=.25,rot=-.25")
            plt.xlabel('')
            plt.ylabel('Economic freedom, overall index, 2022')
            plt.title('Top 10 Economic Freedom Scores in 2022')
            st.pyplot(viz20.figure)
        st.write("Economic Freedom can be defined as the ability of individual citizens and companies to freely decide where to invest and apply their wealth, which is closely related with how much free market is present within the region (Without limitations and interventions of the State and others). It is possible to observe that among the most permissive countries in the economic field we can find a good deal of the happiest nations. Being able to freely apply your resources and investments seems to be linked with one´s happiness")
    pages = {
        "Happiness & National Wealth": page_plot1,    #names will change, don't worry :)
        "Economic Freedom": page_plot2     #names will change, don't worry :)
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

