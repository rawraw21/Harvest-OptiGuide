import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
from PIL import Image
from sklearn.inspection import permutation_importance
from joblib import Parallel, delayed
from sklearn.ensemble import RandomForestClassifier
import joblib
from joblib import dump
import base64
from PIL import Image
from math import pi


pd.options.display.max_colwidth = 2000
st.set_page_config(
    page_title="Crop Recommendation System",
    
    layout="wide",
    initial_sidebar_state="expanded",
)

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-color: #98FB98; /* Warna hijau muda */
}}
[data-testid="stSidebar"] {{
    background-color: #D2B48C; /* Warna coklat muda */
}}
[data-testid="stHeader"] {{
    background-color: #98FB98; /* Warna hijau muda */
}}
[data-testid="stToolbar"] {{
    background-color: #98FB98; /* Warna hijau muda */
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)


def load_bootstrap():
        return st.markdown("""<link rel="stylesheet" 
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
        crossorigin="anonymous">""", unsafe_allow_html=True)

with st.sidebar:
    
    load_bootstrap()

    image_path = r'E:\III RPLK\Pemrograman Paralel\Crop_Recommendation_System-main\Crop_Recommendation_System-main\logo.png'
    image = Image.open(image_path)
    st.image(image, caption='Logo Harvest Opti Guide', use_column_width=True)

    st.markdown("""<h4 style='text-align: center; color: black;'>
    Aplikasi ini dikembangkan oleh Rheva Anindya Wijayanti. 
    Anda dapat menghubungi saya melalui Linkedin and Gmail dibawah:</h4>""",unsafe_allow_html=True)

    st.markdown(f"""<h4 style='text-align: center; color: black;'>
     <a style='text-align: center; color: black;' type="button" class="btn btn-warning btn-lg" 
     href = "https://mail.google.com/mail/u/0/?fs=1&to=rhevaanindyaw@gmail.com&tf=cm">Gmail</a> <a style='text-align: center; color: black;' 
     type="button" class="btn btn-warning btn-lg" 
     href = "https://www.linkedin.com/in/rheva-anindya-wijayanti-6473b2253">Linkedin</a></h4>""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>🌱Harvest Opti Guide🌱</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Sistem Pintar Rekomendasi Pertanian</h1>", unsafe_allow_html=True)


st.markdown("<h5 style='text-align: center;'>Aplikasi ini memprediksi tanaman terbaik yang harus ditanam berdasarkan nilai NPK dan kondisi cuaca 🌦️ !</h5>", unsafe_allow_html= True)

colx, coly, colz = st.columns([1,4,1], gap = 'medium')
with coly:
    st.markdown("""
  
    
      <h6 style='text-align: center;'>
        Aplikasi ini merupakan model Random Forest yang memberikan 
        rekomendasi kepada para petani berdasarkan Dataset Rekomendasi 
        Tanaman 📊 <a style='text-align: center; color: blue;' 
        href="https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset">Dataset</a>.
        Dengan memasukkan nilai N, P, K dan pH berdasarkan kondisi tanah
        atau nilai yang diinginkan dari 4 nilai ini (diubah oleh pupuk), serta dengan memberikan 
        kondisi cuaca, seperti suhu, kelembaban, curah hujan, Anda dapat menghasilkan rekomendasi
        tanaman apa yang sebaiknya ditanam! 
      </h6>
  
        """, unsafe_allow_html=True)

df = pd.read_csv('E:\\III RPLK\\Pemrograman Paralel\\Crop_Recommendation_System-main\\Crop_Recommendation_System-main\\Crop_recommendation.csv')
rdf_clf = joblib.load('E:\\III RPLK\\Pemrograman Paralel\\Crop_Recommendation_System-main\\Crop_Recommendation_System-main\\final_rdf_clf.pkl')

X = df.drop('label', axis = 1)
y = df['label']

df_desc = pd.read_csv('E:\\III RPLK\\Pemrograman Paralel\\Crop_Recommendation_System-main\\Crop_Recommendation_System-main\\Crop_Desc.csv', sep = ';', encoding = 'utf-8', encoding_errors = 'ignore')

st.markdown("<h5 style='text-align: center;'>Importance of each Feature in the Model:</h5>", unsafe_allow_html=True)


importance = pd.DataFrame({'Feature': list(X.columns),
                   'Importance(%)': rdf_clf.feature_importances_}).\
                    sort_values('Importance(%)', ascending = True)
importance['Importance(%)'] = importance['Importance(%)'] * 100

colx, coly, colz = st.columns([1,4,1], gap = 'medium')
with coly:
    color_discrete_sequence = '#609cd4'
    fig = px.bar(importance , x = 'Importance(%)', y = 'Feature', orientation= 'h', width = 200, height = 300)
    fig.update_traces(marker_color="#8C564B")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width= True)

st.markdown("<h5 style='text-align: center;'>Disini Anda dapat memasukkan fitur-fiturnya! Dengan cara ini, sistem akan memprediksi tanaman terbaik yang harus ditanam!</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Pada tanda tanya (?) Anda dapat mendapatkan bantuan tentang setiap fitur.</h5>", unsafe_allow_html=True)


col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,4,1,4,1,1], gap = 'medium')

with col3:
    n_input = st.number_input('Masukkan N (kg/ha) value:', min_value= 0, max_value= 140, help = 'Masukkan disini Nitrogen density (kg/ha) dari 0 sampai 140.')
    p_input = st.number_input('Masukkan P (kg/ha) value:', min_value= 5, max_value= 145, help = 'Masukkan disini Phosphorus density (kg/ha) dari 5 sampai 145.')
    k_input = st.number_input('Masukkan K (kg/ha) value:', min_value= 5, max_value= 205, help = 'Masukkan disini Potassium density (kg/ha) dari 5 sampai 205.')
    temp_input = st.selectbox('Pilih Avg Temperature (ºC) value:', options=list(range(4, 44)), format_func=lambda x: f'{x} ºC', help='Pilih disini Avg Temperature (ºC) dari 4 sampai 43.')

with col5:
    hum_input = st.number_input('Masukkan Avg Humidity (%) value:', min_value= 15., max_value= 99., step = 1., format="%.2f", help = 'Masukkan disini Avg Humidity (%) dari 15 sampai 99.')
    ph_input = st.selectbox('Pilih pH value:', options=[round(x, 1) for x in list(np.arange(3.6, 10, 0.1))], format_func=lambda x: f'{x}', help='Pilih disini pH dari 3.6 sampai 9.9.')
    rain_input = st.number_input('Masukkan Avg Rainfall (mm) value:', min_value= 21.0, max_value= 298.0, step = 0.1, format="%.2f", help = 'Masukkan disini Avg Rainfall (mm) dari 21 sampai 298')




predict_inputs = [[n_input,p_input,k_input,temp_input,hum_input,ph_input,rain_input]]

with col5:
    predict_btn = st.button('Get Your Recommendation!')


cola,colb,colc = st.columns([2,10,2])
if predict_btn:
    rdf_predicted_value = rdf_clf.predict(predict_inputs)

    with colb:
        st.markdown(f"<h3 style='text-align: center;'>Best Crop to Plant: {rdf_predicted_value[0]}.</h3>", 
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns([9,4,9])
    with col2:
        df_desc = df_desc.astype({'label':str,'image':str})
        df_desc['label'] = df_desc['label'].str.strip()
        df_desc['image'] = df_desc['image'].str.strip()
        

        df_pred_image = df_desc[df_desc['label'].isin(rdf_predicted_value)]
        df_image = df_pred_image['image'].item()
        
        st.markdown(f"""<h5 style = 'text-align: center; height: 300px; object-fit: contain;'> {df_image} </h5>""", unsafe_allow_html=True)
        

    
    st.markdown(f"""<h5 style='text-align: center;'>Statistics Summary about {rdf_predicted_value[0]} 
            NPK and Weather Conditions values in the Dataset.</h5>""", unsafe_allow_html=True)
    df_pred = df[df['label'] == rdf_predicted_value[0]]
    st.dataframe(df_pred.describe(), use_container_width = True)       



if predict_btn:
    rdf_predicted_value = rdf_clf.predict(predict_inputs)


    df_line_chart = pd.DataFrame({
        'Parameter': ['N', 'P', 'K', 'Temperature', 'Humidity', 'pH', 'Rainfall'],
        'Value': [n_input, p_input, k_input, temp_input, hum_input, ph_input, rain_input]
    })

    fig_line_chart = px.line(df_line_chart, x='Parameter', y='Value', markers=True, labels={'Value': 'Parameter Value'})
    fig_line_chart.update_traces(line=dict(color='red'))

    fig_line_chart.update_layout(
        title='Changes in Weather and Soil Nutrient Values',
        xaxis_title='Parameter',
        yaxis_title='Value',
    )

    st.plotly_chart(fig_line_chart, use_container_width=True)


