import streamlit as st
import seaborn as sns
import pandas as pd
st.title("Evolution of World Happiness")
st.write("In this project we want to analisys the **World Happiness** in the last years and try to understand what contribute or not to the results")
st.sidebar.header("What should we know about the World Hapiness")
st.sidebar.slider('Select the Year', 2015, 2021)