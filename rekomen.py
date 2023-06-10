import streamlit as st
import pandas as pd


# Tampilkan judul aplikasi
st.title('Sistem Rekomendasi Film')

#upload file dataset 
uploaded_file = st.file_uploader('upload dataset film', type=['csv'])

# Jika file dataset diupload
if uploaded_file is not None:
    # Baca file dataset menjadi DataFrame
    df_movies = pd.read_csv(uploaded_file)
