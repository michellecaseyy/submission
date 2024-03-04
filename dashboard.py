import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

bike_df = pd.read_csv("https://raw.githubusercontent.com/michellecaseyy/submission/main/day.csv")
bike_df["dteday"] = pd.to_datetime(bike_df["dteday"])
bike_df.rename(columns={
    "cnt": "user_count",
    "mnth": "month"
}, inplace=True)

min_date = bike_df["dteday"].min()
max_date = bike_df["dteday"].max()
 
with st.sidebar:
    st.header("Bike Sharing Dataset")
    st.write("Tanggal awal pengambilan data : ", min_date)
    st.write("Tanggal akhir pengambilan data : ", max_date)

st.header('Bike Rental Data Analysis :sparkles:')
st.subheader('1. Komposisi Tipe Penyewa')
col1, col2 = st.columns(2)
 
with col1:
    st.metric("Registered", value=bike_df['registered'].sum())
 
with col2: 
    st.metric("Casual", value=bike_df['casual'].sum())

cat = ('Registered Users', 'Casual Users')
count = (bike_df['registered'].sum(), bike_df['casual'].sum())
colors = ("#E1AFD1", "#FFE6E6")
explode = (0.1, 0)
fig, ax = plt.subplots(figsize=(2, 2))
ax.pie(count, labels=cat, autopct='%1.1f%%', colors=colors, explode=explode)
st.pyplot(fig)

by_season_df = bike_df.groupby(by="season").user_count.sum().sort_values(ascending=False).reset_index()
by_season_df["season"] = by_season_df["season"].astype(str)
season_map = {"1": "Spring", "2": "Summer", "3": "Fall", "4": "Winter"}
by_season_df["season"] = by_season_df["season"].map(season_map)
colors1_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

by_month_df = bike_df.groupby(by="month").user_count.sum().reset_index()
by_month_df["month"] = by_month_df["month"].astype(str)
month_map = {"1": "Jan", "2": "Feb", "3": "Mar", "4": "Apr","5": "May", "6": "Jun", "7": "Jul", "8": "Aug","9": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
by_month_df["month"] = by_month_df["month"].map(month_map)
colors2_ = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3","#72BCD4", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3"]

by_weather_df = bike_df.groupby(by="weathersit").user_count.sum().sort_values(ascending=False).reset_index()
colors3_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

st.subheader("2. Jumlah Sewa Sepeda Terbanyak Berdasarkan Kategori")
 
fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(35, 60))
 
sns.barplot(x="season", y="user_count", data=by_season_df, palette=colors1_, ax=ax[0])
ax[0].set_ylabel("Jumlah penyewa (juta)", fontsize = 35)
ax[0].set_xlabel(None)
ax[0].set_title("Jumlah Rental Berdasarkan Musim", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=35)

sns.barplot(x="month", y="user_count", data=by_month_df, palette=colors2_, ax=ax[1])
ax[1].set_ylabel("Jumlah penyewa", fontsize = 35)
ax[1].set_xlabel(None)
ax[1].set_title("Jumlah Rental Berdasarkan Bulan", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=35)

sns.barplot(x="weathersit", y="user_count", data=by_weather_df, palette=colors3_, ax=ax[2])
ax[2].set_ylabel("Jumlah penyewa (juta)", fontsize = 35)
ax[2].set_xlabel(None)
ax[2].set_title("Jumlah Rental Berdasarkan Cuaca", loc="center", fontsize=50)
ax[2].tick_params(axis='y', labelsize=35)
ax[2].tick_params(axis='x', labelsize=35)
 
st.pyplot(fig)

st.write("1: Clear, Few clouds, Partly cloudy, Partly cloudy")
st.write("2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
st.write("3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
