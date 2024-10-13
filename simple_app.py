
# Import necessary libraries for data visualization and web app

import streamlit as st
import plotly.express as px
import seaborn as sns
import numpy as np

# Load the dataset
tips = sns.load_dataset('tips')

# Visualizations using Plotly

fig1 = px.bar(tips, x="day", y="tip")

fig2 = px.violin(tips, x="sex", y="tip")

# Streamlit web app layout
st.title("Data Visualization with Plotly")

# Section 1: Bar Plot

st.header("Plot 1: Bar Plot - Tips by Day")
st.plotly_chart(fig1)
st.markdown('''**Insight Observed**: (Add your insights here)''')

# Section 2: Violin Plot

st.header("Plot 2: Violin Plot - Tips by Gender")
st.plotly_chart(fig2)
st.markdown('''**Insight Observed**: (Add your insights here)''')
