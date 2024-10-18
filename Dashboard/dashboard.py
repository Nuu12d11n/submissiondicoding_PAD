import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_data = pd.read_csv('dataanalis_bike.csv')
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
weather_data = day_data.groupby('weathersit')['cnt'].mean().reset_index()
sns.barplot(x='weathersit', y='cnt', data=weather_data)
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Cuaca')
st.pyplot()

# Pertanyaan 2: Penyewaan pada Hari Kerja vs Akhir Pekan
st.subheader("Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan")
day_data['day_type'] = day_data['weekday'].apply(lambda x: 'Akhir Pekan' if x in [0, 6] else 'Hari Kerja')
day_type_data = day_data.groupby('day_type')['cnt'].mean().reset_index()
sns.barplot(x='day_type', y='cnt', data=day_type_data)
plt.title('Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
st.pyplot()
