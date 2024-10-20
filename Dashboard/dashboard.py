import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_data = pd.read_csv('Dashboard/hasil_analisis.csv')
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

# Membuat plot rata-rata penyewaan berdasarkan cuaca
fig1, ax1 = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weather_data, ax=ax1, order=weather_order, 
            palette=['#ffdd57', '#66b2ff', '#ff6666'])  # Warna: kuning, biru, merah
ax1.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Cuaca')
ax1.set_xlabel('Cuaca')
ax1.set_ylabel('Rata-rata Jumlah Penyewaan')

# Menampilkan plot di Streamlit
st.pyplot(fig1)

# Menambahkan visualisasi histogram untuk distribusi penyewaan sepeda
st.subheader("Distribusi Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan")
plt.figure(figsize=(10, 5))

# Membuat histogram dengan bins yang konsisten
sns.histplot(data=day_data[day_data['workingday'] == 0], x='cnt', color='blue', alpha=0.5, label='Akhir Pekan', bins=30, stat="count")
sns.histplot(data=day_data[day_data['workingday'] == 1], x='cnt', color='green', alpha=0.5, label='Hari Kerja', bins=30, stat="count")

# Menambahkan judul dan label
plt.title('Distribusi Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan', fontsize=14)
plt.xlabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)

# Menambahkan legenda
plt.legend(title='Jenis Hari', labels=['Akhir Pekan', 'Hari Kerja'])

# Mengatur layout agar tidak terpotong
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(plt)
