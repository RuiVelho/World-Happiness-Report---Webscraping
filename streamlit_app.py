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
    initial_sidebar_state="expanded",
)
#st.title("Evolution of World Happiness")
#st.write("In this project we want to analyze the **World Happiness** in the last years and try to understand what contribute to the results")
st.sidebar.header("World Happiness Analysis\n `2018 and 2019`")
#st.sidebar.slider('Select the Year', 2015, 2021)
#dataset will come here:
df2019 = pd.read_csv("https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2019.csv")
df2018 = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2018.csv')
df_hd=pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/df_hd.csv')
df2015 = pd.read_csv("https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/2015.csv")


choice = st.sidebar.radio("Select the Topic", ('Overall Happiness','Happiness by Region','Wealth Potential','Social Support','Human Development'))
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
    st.header("Happiness by Region 2019")
    #st.subheader("Here some explanation")
    def page_plot1():
        col1, col2 = st.columns(2)
        with col1:
            #st.write("here column 1")
            df2019_mean_region = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/df2019_mean_region.csv')
            #some graphs or tables
            fig, ax = plt.subplots(1,1)
            plt.rcParams['figure.figsize']=(15,7)
            viz_1 = sns.barplot(y = df2019_mean_region.Region,
                                x = df2019_mean_region.happiness_score,
                                orient='h',
                                palette="ch:s=.25,rot=-.25",
                                ax=ax)
            plt.title("Average Happiness Score per Region", fontsize=20)
            plt.xlabel("Average Happiness Score", fontsize=14) 
            plt.ylabel("")
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=18)
            plt.xlim(left=4)
            plt.grid(axis='x', alpha=.3)
            st.pyplot(viz_1.figure)
            # second graph: move it somewhere else #
            df2019_range = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/df2019_range.csv')
            fig, ax = plt.subplots(1,1)
            plt.rcParams['figure.figsize']=(15,7)
            viz_3 = sns.barplot(y = df2019_range.Region,
                                x = df2019_range.happiness_score,
                                orient='h',
                                palette="ch:s=.25,rot=-.25",
                                ax=ax)
            plt.title("Range of Happiness Score per Region", fontsize=20)
            plt.xlabel("Range of Happiness Score", fontsize=14) 
            plt.ylabel("")
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=18)
            plt.grid(axis='x', alpha=.3)
            st.pyplot(viz_3.figure)
        with col2:
            #st.write("here column 2")
            df2019_happinest_6 = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/df2019_happinest_6.csv')
            #some graphs or tables
            fig, ax = plt.subplots(1,1)
            plt.rcParams['figure.figsize']=(15,7)
            viz_2 = sns.barplot(y = df2019_happinest_6.Region,
                                x = df2019_happinest_6.happiness_score,
                                orient='h',
                                palette="ch:s=.25,rot=-.25",
                                ax=ax)
            plt.title("Happiness score above 6.0", fontsize=20)
            plt.xlabel("Number of countries", fontsize=14) 
            plt.ylabel("")
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=18)
            plt.xticks([0, 3, 6, 9, 12, 15, 18])
            plt.grid(axis='x', alpha=.3)
            st.pyplot(viz_2.figure)

    def page_plot2():
        # scatterplots
        df2019_regional = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/df2019_regional.csv')
        #selected_region = st.select_slider('Select Region', options=list(set(df2019_regional['Region']))+['All regions'])
        selected_region = st.radio('Select Region', options=['All regions']+list(set(df2019_regional['Region'])), horizontal=True)
        if selected_region=='All regions':
            filtered_data = df2019_regional
        else:
            filtered_data = df2019_regional[df2019_regional['Region']==selected_region]
        col1, col2 = st.columns(2)
        with col1:     
            #st.write("here column 1")
            fig, ax = plt.subplots(1,1)
            plt.rcParams['figure.figsize']=(15,7)
            viz_s1 = sns.scatterplot(filtered_data,
                y='social_support',
                x='happiness_score',
                hue='Region',
                s=200,
                ax=ax)
            plt.title("Social Support - Happiness Score", fontsize=20)
            plt.legend(loc='lower right', fontsize='12')
            plt.ylabel("Social Support", fontsize=14) 
            plt.xlabel("Happiness Score", fontsize=14)
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=18)
            st.pyplot(viz_s1.figure)
  
        with col2:
            #st.write("here column 2")
            fig, ax = plt.subplots(1,1)
            plt.rcParams['figure.figsize']=(15,7)
            viz_s2 = sns.scatterplot(filtered_data,
                y='gdp_per_capita',
                x='happiness_score',
                hue='Region',
                s=200,
                ax=ax)
            plt.title("GDP - Happiness Score", fontsize=20)
            plt.legend(loc='lower right', fontsize='12')
            plt.ylabel("GDP per capita", fontsize=14) 
            plt.xlabel("Happiness Score", fontsize=14)
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=18)
            st.pyplot(viz_s2.figure)
            # second plot
            fig, ax = plt.subplots(1,1)
            plt.rcParams['figure.figsize']=(15,7)
            viz_s3 = sns.scatterplot(filtered_data,
                y='healthy_life_expectancy',
                x='happiness_score',
                hue='Region',
                s=200,
                ax=ax)
            plt.title("Life Expectancy - Happiness Score", fontsize=20)
            plt.legend(loc='lower right', fontsize='12')
            plt.ylabel("Healthy Life Expectancy", fontsize=14) 
            plt.xlabel("Happiness Score", fontsize=14)
            plt.xticks(fontsize=14)
            plt.yticks(fontsize=18)
            st.pyplot(viz_s3.figure)

    def page_plot3():
        col1, col2 = st.columns(2)
        with col1:     
            # heatmap
            dropped_df2019 = df2019.drop(columns=['Overall rank'])
            fig, ax = plt.subplots(1,1)
            viz_corr = sns.heatmap(dropped_df2019.corr(),
                                   cmap = 'RdBu_r',
                                   square =True,
                                   ax=ax)
            plt.title('Heatmap 2019')
            st.pyplot(viz_corr.figure)   
            
    pages = {
        "Further Happiness Analysis": page_plot1,
        "Correlations": page_plot2,
        "Heatmap": page_plot3
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
        # web scraping graph: move to the first section
        df_health10_ws = pd.read_csv('https://raw.githubusercontent.com/MauricioConceicao123/World-Happiness-Report---Webscraping/main/df_health10_ws.csv')
        fig, ax = plt.subplots(1,1)
        viz_ws = sns.barplot(df_health10_ws,
                                 y='Countries', 
                                 x='Health spending as percent of GDP, 2019',
                                 palette="ch:s=.25,rot=-.25")
        plt.title("Health spending as percent of GDP, 2019", fontsize=20)
        plt.xlabel("") 
        plt.ylabel("")
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=18)
        plt.xlim(left=8)
        plt.grid(axis='x', alpha=.3) 
        st.pyplot(viz_ws.figure)
    pages = {
        "Happiness & National Wealth": page_plot1,    #names will change, don't worry :)
        "Economic Freedom and Health Spending": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Social Support':
    st.header("World Happiness Analysis")
    def page_plot1():
        st.subheader("Top 10 Country with the Best Social Support")
        col1, col2 = st.columns(2)
        with col1:
            df2018.sort_values('Social support', ascending=False, inplace=True)
            socialsuport=df2018.head(10)
            fig, ax=plt.subplots(figsize=(8,5))
            viz1=sns.barplot(socialsuport, x='Country or region', y='Social support', palette="ch:s=.25,rot=-.25", ax=ax)
            ax.bar_label(ax.containers[0])
            ax.set_xticklabels(socialsuport['Country or region'], rotation=45)
            ax.set(title="2018")
            ax.set_xlabel('')
            ax.set_ylabel('Rate Social Support')
            ax.set_ylim(bottom=1.4)
            st.pyplot(viz1.figure)
        with col2:
            df2019.sort_values('Social support', ascending=False, inplace=True)
            ss2019=df2019.head(10)
            fig, ax=plt.subplots(figsize=(8,5))
            viz2=sns.barplot(ss2019, x='Country or region', y='Social support', palette="flare", ax=ax)
            ax.bar_label(ax.containers[0])
            ax.set_xticklabels(ss2019['Country or region'], rotation=45)
            ax.set(title="2019")
            ax.set_xlabel('')
            ax.set_ylabel('Rate Social Support')
            ax.set_ylim(bottom=1.4)
            st.pyplot(viz2.figure)
    def page_plot2():
        st.subheader("Top 10 Country with the Best Values of GDP per Capita")
        col1, col2 = st.columns(2)
        with col1:
            df2018.sort_values('GDP per capita', ascending=False, inplace=True)
            gdp2018=df2018.head(10)
            fig, ax1=plt.subplots(figsize=(8,5))
            viz3=sns.barplot(gdp2018, x='Country or region', y='GDP per capita', palette="ch:s=.25,rot=-.25", ax=ax1)
            ax1.bar_label(ax1.containers[0])
            ax1.set_xticklabels(gdp2018['Country or region'], rotation=45)
            ax1.set(title="2018")
            ax1.set_xlabel('')
            st.pyplot(viz3.figure)
        with col2:
            df2019.sort_values('GDP per capita', ascending=False, inplace=True)
            gdp2019=df2019.head(10)
            fig, ax4=plt.subplots(figsize=(8,5))
            viz4=sns.barplot(gdp2019, x='Country or region', y='GDP per capita', palette="flare", ax=ax4)
            ax4.bar_label(ax4.containers[0])
            ax4.set_xticklabels(gdp2019['Country or region'], rotation=45)
            ax4.set(title="2019")
            ax4.set_xlabel('')
            st.pyplot(viz4.figure)
    pages = {
        "Social Support": page_plot1,    #names will change, don't worry :)
        "The Best Values of GDP per Capita": page_plot2     #names will change, don't worry :)
    }
    selected_page = st.selectbox(
        "Choose Page",
        pages.keys()
    )
    pages[selected_page]()
if choice == 'Human Development':
    st.header("Top 10 Countries Ratio of Commitment to Human Development")
    fig, ax5= plt.subplots(figsize=(6,3))
    viz5=sns.barplot(df_hd, x='Countries', y='Human development, 2021', palette="ch:s=.25,rot=-.25")
    ax5.set_xticklabels(df_hd['Countries'], rotation=45)
    ax5.set_ylim(bottom=0.8)
    ax5.set_yticklabels(['{:,.2f}'.format(y) for y in ax5.get_yticks()])
    ax5.set_ylabel('')
    for container in ax5.containers:
        ax5.bar_label(container, label_type='edge', labels=['{:,.2f}'.format(val) for val in container.datavalues])
    ax5.set_xlabel('')
    ax5.set(title="2021")
    st.pyplot(viz5.figure)

    st.write("here column 1")

