import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Crop_recommendation.csv")


st.sidebar.title("Informasi Dataset")
st.sidebar.text("Jumlah jenis tanaman: {}".format(df['label'].nunique()))
st.sidebar.text("Ringkasan Dataset:")
st.sidebar.write(df.describe())


st.title("Eksplorasi Dataset Rekomendasi Tanaman")


st.subheader("Dataset Rekomendasi Tanaman")
st.dataframe(df)



st.subheader("Histogram untuk N, P, K")
selected_elements = st.multiselect("Pilih elemen", ["N", "P", "K"])
colors = sns.color_palette("husl", len(selected_elements))
fig, ax = plt.subplots(figsize=(10, 6))
for selected_element, color in zip(selected_elements, colors):
    sns.histplot(df[selected_element], color=color, kde=True, ax=ax, label=selected_element)
ax.set_title('Histogram for N, P, K')
ax.legend()
st.pyplot(fig)


st.subheader("Histogram untuk pH, Temperature, Humidity, Rainfall")
selected_weathers = st.multiselect("Pilih parameter cuaca", ["ph", "temperature", "humidity", "rainfall"])
colors_weather = sns.color_palette("husl", len(selected_weathers))
fig, ax = plt.subplots(figsize=(10, 6))
for selected_weather, color in zip(selected_weathers, colors_weather):
    sns.histplot(df[selected_weather], color=color, kde=True, ax=ax, label=selected_weather)
ax.set_title('Histogram untuk pH, Temperature, Humidity, Rainfall')
ax.legend()
st.pyplot(fig)


st.subheader("NPK Means by Crop")
crop_desc = pd.pivot_table(df, index='label', aggfunc='mean')
crop_desc.reset_index(inplace=True)
st.dataframe(crop_desc)


st.subheader("Bar Chart unntuk NPK Means by Crop")
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


st.subheader("Boxplot - pH by Crop")
fig, ax = plt.subplots(figsize=(18, 5))
ph_boxplot = sns.boxplot(data=df, x='label', y='ph')
ph_boxplot.set_xlabel('Crop', fontsize=14)
ph_boxplot.set_ylabel('pH', fontsize=14)
ph_boxplot.axes.set_title('Boxplot - pH by Crop', fontsize=14)
ph_boxplot.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)


st.subheader("Korelasi antara Fitur Numerik")
fig, ax = plt.subplots(figsize=(15, 9))
sns.heatmap(df.drop('label', axis=1).corr(), annot=True, cmap='crest')
ax.set(xlabel='Features', ylabel='Features')
plt.title('Korelasi antara Fitur Numerik')
st.pyplot(fig)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
