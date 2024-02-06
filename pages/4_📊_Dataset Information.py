import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Sidebar with dataset info
st.sidebar.title("Dataset Information")
st.sidebar.text("Number of Crop types: {}".format(df['label'].nunique()))
st.sidebar.text("Dataset Summary:")
st.sidebar.write(df.describe())

# Main page title
st.title("Crop Recommendation Dataset Exploration")

# Display the dataset
st.subheader("Crop Recommendation Dataset")
st.dataframe(df)

# Exploratory Data Analysis
# Plot histograms for N, P, K
st.subheader("Histograms for N, P, K")
selected_elements = st.multiselect("Select elements", ["N", "P", "K"])
colors = sns.color_palette("husl", len(selected_elements))
fig, ax = plt.subplots(figsize=(10, 6))
for selected_element, color in zip(selected_elements, colors):
    sns.histplot(df[selected_element], color=color, kde=True, ax=ax, label=selected_element)
ax.set_title('Histogram for N, P, K')
ax.legend()
st.pyplot(fig)

# Plot histograms for pH, temperature, humidity, rainfall
st.subheader("Histograms for pH, Temperature, Humidity, Rainfall")
selected_weathers = st.multiselect("Select weather parameters", ["ph", "temperature", "humidity", "rainfall"])
colors_weather = sns.color_palette("husl", len(selected_weathers))
fig, ax = plt.subplots(figsize=(10, 6))
for selected_weather, color in zip(selected_weathers, colors_weather):
    sns.histplot(df[selected_weather], color=color, kde=True, ax=ax, label=selected_weather)
ax.set_title('Histogram for pH, Temperature, Humidity, Rainfall')
ax.legend()
st.pyplot(fig)

# Pivot table for NPK means by Crop
st.subheader("NPK Means by Crop")
crop_desc = pd.pivot_table(df, index='label', aggfunc='mean')
crop_desc.reset_index(inplace=True)
st.dataframe(crop_desc)

# Bar chart for NPK means by Crop
st.subheader("Bar Chart for NPK Means by Crop")
labels = crop_desc['label'].unique()
n_value = crop_desc['N']
p_value = crop_desc['P']
k_value = crop_desc['K']

fig, ax = plt.subplots(figsize=(17, 7))
n_bar = ax.bar(labels, n_value, label='N')
p_bar = ax.bar(labels, p_value, bottom=n_value, label='P')
k_bar = ax.bar(labels, k_value, bottom=n_value + p_value, label='K')

ax.set_ylabel('kg/ha (Mean)')
ax.set_title('NPK Means by Crop')
ax.legend()

st.pyplot(fig)

# Boxplot for pH by Crop
st.subheader("Boxplot - pH by Crop")
fig, ax = plt.subplots(figsize=(18, 5))
ph_boxplot = sns.boxplot(data=df, x='label', y='ph')
ph_boxplot.set_xlabel('Crop', fontsize=14)
ph_boxplot.set_ylabel('pH', fontsize=14)
ph_boxplot.axes.set_title('Boxplot - pH by Crop', fontsize=14)
ph_boxplot.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Correlation heatmap
st.subheader("Correlation between Numeric Features")
fig, ax = plt.subplots(figsize=(15, 9))
sns.heatmap(df.drop('label', axis=1).corr(), annot=True, cmap='crest')
ax.set(xlabel='Features', ylabel='Features')
plt.title('Correlation between Numeric Features')
st.pyplot(fig)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
