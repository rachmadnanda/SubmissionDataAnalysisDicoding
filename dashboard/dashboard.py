import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Air Quality Dashboard", page_icon="🌤️", layout="wide")

# 2. Fungsi Load Data 
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(current_dir, 'main_data.csv')
    
    df = pd.read_csv(file_path)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

df = load_data()

# 3. Sidebar untuk Filter Interaktif
st.sidebar.header("Filter Data")
min_year = df['year'].min()
max_year = df['year'].max()
selected_year = st.sidebar.slider("Pilih Rentang Tahun", min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Menyaring dataset berdasarkan input slider
filtered_df = df[(df['year'] >= selected_year[0]) & (df['year'] <= selected_year[1])]

# 4. Bagian Utama Dashboard
st.title("🌤️ Air Quality Data Analysis: Stasiun Wanliu")
st.markdown("Dashboard ini menyajikan hasil analisis kualitas udara di Stasiun Wanliu berdasarkan parameter polutan dan cuaca.")

# Menampilkan metrik ringkasan
col1, col2, col3 = st.columns(3)
col1.metric("Rata-rata Polusi PM2.5", f"{filtered_df['PM2.5'].mean():.2f} µg/m³")
col2.metric("Suhu Rata-rata", f"{filtered_df['TEMP'].mean():.2f} °C")
col3.metric("Kecepatan Angin Maks", f"{filtered_df['WSPM'].max():.2f} m/s")

st.divider()

# Menampilkan Raw Data jika dicentang
if st.checkbox("Tampilkan Cuplikan Data (Cleaned)"):
    st.dataframe(filtered_df.head(10))

# 5. Visualisasi dalam Tabs
tab1, tab2, tab3 = st.tabs([
    "📈 Tren PM2.5 Bulanan (Q1)", 
    "🌡️ Korelasi Parameter (Q2)", 
    "📊 Kategori Kualitas Udara (Advanced)"
])

# -- TAB 1: Tren Rata-rata Bulanan PM2.5 --
with tab1:
    st.subheader(f"Tren Konsentrasi PM2.5 ({selected_year[0]} - {selected_year[1]})")
    df_monthly = filtered_df.resample('M', on='datetime')['PM2.5'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=df_monthly, x='datetime', y='PM2.5', marker='o', color='crimson', ax=ax)
    ax.set_xlabel("Waktu (Tahun-Bulan)")
    ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    st.info("**Insight:** Tren menunjukkan bahwa polusi udara (PM2.5) cenderung memburuk pada musim dingin (menjelang akhir dan awal tahun).")

# -- TAB 2: Korelasi Parameter (Heatmap) --
with tab2:
    st.subheader("Korelasi PM2.5 dengan Suhu dan Kecepatan Angin")
    corr_matrix = filtered_df[['PM2.5', 'TEMP', 'WSPM']].corr()

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax2)
    st.pyplot(fig2)
    st.info("**Insight:** Terdapat korelasi negatif antara PM2.5 dengan Kecepatan Angin (WSPM). Semakin kencang angin, polusi cenderung berkurang.")

# -- TAB 3: Kategori Kualitas Udara (Analisis Lanjutan / Binning) --
with tab3:
    st.subheader("Distribusi Kategori Kualitas Udara (PM2.5 Index)")
    
    # Binning
    bins = [0, 35, 75, 150, 500, 1000]
    labels = ['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
    filtered_df['Air_Quality'] = pd.cut(filtered_df['PM2.5'], bins=bins, labels=labels)

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.countplot(data=filtered_df, x='Air_Quality', palette='viridis', ax=ax3)
    ax3.set_xlabel("Kategori")
    ax3.set_ylabel("Jumlah Jam (Pengamatan)")
    st.pyplot(fig3)
    st.info("**Insight:** Mayoritas kualitas udara berada di level *Good* hingga *Unhealthy*. Namun, terdapat beberapa kondisi ekstrem (*Hazardous*) yang terekam.")