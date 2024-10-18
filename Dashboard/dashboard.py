import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_data = pd.read_csv('Dashboard/dataanalis_bike.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Mengganti nilai di kolom 'weathersit'
weather_mapping = {1: 'Cerah', 2: 'Sedang', 3: 'Hujan'}
day_data['weathersit'] = day_data['weathersit'].map(weather_mapping)

# Set title
st.title("Dashboard Penyewaan Sepeda")

# Menampilkan data
if st.checkbox("Tampilkan Data"):
    st.subheader("Data Penyewaan Sepeda")
    st.write(day_data)

# Pertanyaan 1: Pengaruh Cuaca
st.subheader("Pengaruh Cuaca Terhadap Penyewaan Sepeda")

# Mengatur urutan cuaca menjadi Cerah, Sedang, Hujan
weather_data = day_data.groupby('weathersit')['cnt'].mean().reset_index()
weather_order = ['Cerah', 'Sedang', 'Hujan']  # Urutan cuaca yang diinginkan

# Membuat plot
fig1, ax1 = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weather_data, ax=ax1, order=weather_order, 
            palette=['#ffdd57', '#66b2ff', '#ff6666'])  # Warna: kuning, biru, merah
ax1.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Cuaca')
ax1.set_xlabel('Cuaca')
ax1.set_ylabel('Rata-rata Jumlah Penyewaan')

# Menampilkan plot di Streamlit
st.pyplot(fig1)


# Menggunakan KDE plot untuk menampilkan distribusi kepadatan
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.kdeplot(data=day_data, x='cnt', hue='workingday', fill=True, ax=ax2, palette='Set1')

# Menambahkan judul dan label
ax2.set_title('Kepadatan Distribusi Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan', fontsize=14)
ax2.set_xlabel('Jumlah Penyewaan Sepeda', fontsize=12)
ax2.set_ylabel('Kepadatan', fontsize=12)
ax2.legend(labels=['Akhir Pekan', 'Hari Kerja'])

st.pyplot(fig2)

