import streamlit as st
from PIL import Image

brown_text = '<h1 style="color:brown;">About</h1>'

st.markdown(brown_text, unsafe_allow_html=True)

image_path = r'gambar.png'
image = Image.open(image_path)
st.image(image, use_column_width=True)

st.write("""
🌿 **Mengoptimalkan Pertanian dengan Aplikasi Rekomendasi Tanaman Berbasis Model Random Forest** 🌿

Dalam dunia pertanian yang terus berkembang, teknologi semakin memainkan peran kunci untuk meningkatkan hasil panen dan efisiensi pertanian. Salah satu inovasi terbaru adalah penggunaan model Random Forest dalam Aplikasi Rekomendasi Tanaman. 📊

Aplikasi ini dirancang untuk memberikan panduan kepada para petani dengan mengandalkan Dataset Rekomendasi Tanaman yang kaya informasi. Bagaimana caranya? Mari kita telusuri bersama!

**Langkah 1: Input Data Tanah 🌱**
Petani cukup memasukkan nilai N (Nitrogen), P (Fosfor), K (Kalium), dan pH tanah mereka. Nilai-nilai ini mencerminkan kondisi tanah atau keinginan untuk mengubahnya melalui pemakaian pupuk. Dengan informasi ini, model Random Forest dapat memberikan rekomendasi tanaman yang paling sesuai.

**Langkah 2: Faktor Cuaca 🌦️**
Selain dari kondisi tanah, Aplikasi Rekomendasi Tanaman juga memperhitungkan faktor cuaca. Suhu, kelembaban, dan curah hujan menjadi pertimbangan penting. Dengan memasukkan data cuaca saat ini, petani bisa mendapatkan rekomendasi tanaman yang optimal sesuai dengan kondisi lingkungan mereka.

**Langkah 3: Visualisasi dengan Chart 📈**
Untuk memberikan gambaran yang lebih jelas, aplikasi menyajikan hasilnya dalam bentuk diagram garis. 🌾 Chart ini dengan sederhana menjelaskan seberapa besar pengaruh masing-masing faktor seperti Nitrogen, Fosfor, Kalium, dan pH terhadap rekomendasi tanaman yang diberikan oleh model Random Forest.

Dengan pendekatan yang inovatif ini, para petani dapat dengan mudah mengakses rekomendasi yang disesuaikan dengan kondisi unik tanah dan cuaca mereka. 🌍 Hasil panen yang lebih baik dan pertanian yang efisien adalah tujuan utama dari Aplikasi Rekomendasi Tanaman ini.

Jadi, mari kita bersama-sama memasuki era pertanian yang cerdas dan efisien dengan teknologi yang melayani petani dan bumi kita. 🚜✨
""")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("E:\\III RPLK\\Pemrograman Paralel\\Crop_Recommendation_System-main\\Crop_Recommendation_System-main\\style.css")
