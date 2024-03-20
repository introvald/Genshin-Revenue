import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title='Genshin Revenue')
st.header('Genshin Revenue from Version 1.0 - 3.3')
st.subheader('Version 1.0-3.3')

df = pd.read_csv('dataset.csv')

def bar_plot(data):
    plt.bar(data["version"], data["revenue"])
    plt.xlabel("Version")
    plt.ylabel("Revenue")
    plt.title("Revenue by Version")
    st.pyplot()

bar_plot(df)

st.write(df)
