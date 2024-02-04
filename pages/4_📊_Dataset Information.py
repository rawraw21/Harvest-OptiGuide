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
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(df['N'], color='blue', kde=True, ax=ax1)
ax1.set_title('Histogram for N')

sns.histplot(df['P'], color='red', kde=True, ax=ax2)
ax2.set_title('Histogram for P')

sns.histplot(df['K'], color='green', kde=True, ax=ax3)
ax3.set_title('Histogram for K')

st.pyplot(fig)

# Plot histograms for pH, temperature, humidity, rainfall
st.subheader("Histograms for pH, Temperature, Humidity, Rainfall")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 8))

sns.histplot(df['ph'], color='blue', kde=True, ax=ax1)
ax1.set_title('Histogram for pH')

sns.histplot(df['temperature'], color='red', kde=True, ax=ax2)
ax2.set_title('Histogram for Temperature')

sns.histplot(df['humidity'], color='purple', kde=True, ax=ax3)
ax3.set_title('Histogram for Humidity')

sns.histplot(df['rainfall'], color='green', kde=True, ax=ax4)
ax4.set_title('Histogram for Rainfall')

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


local_css("E:\\III RPLK\\Pemrograman Paralel\\Crop_Recommendation_System-main\\Crop_Recommendation_System-main\\style.css")
