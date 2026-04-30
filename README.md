# 🌤️ Air Quality Analysis Dashboard: Stasiun Wanliu

Selamat datang di proyek **Air Quality Analysis Dashboard**! 🚀  
Proyek ini merupakan submission untuk kelas **Belajar Analisis Data dengan Python** dari Dicoding. Dashboard interaktif ini dibuat menggunakan Streamlit untuk mengeksplorasi dan menganalisis tren kualitas udara, khususnya konsentrasi PM2.5, hubungannya dengan cuaca, serta status kualitas udara di Stasiun Wanliu.

---

## 📌 Fitur Dashboard

- **Filter Tahun Interaktif:** Menyesuaikan rentang waktu analisis sesuai kebutuhan.
- **Tren PM2.5 Bulanan:** Visualisasi pergerakan polusi udara secara _time-series_.
- **Analisis Korelasi:** Memahami dampak Suhu (TEMP) dan Kecepatan Angin (WSPM) terhadap tingkat polusi.
- **Kategori Kualitas Udara (AQI):** Pengelompokan level polusi melalui teknik _Binning_ / _Clustering_ sederhana.

---

## 📂 Struktur Direktori

```text
├── dashboard/
│   ├── dashboard.py                            <- Entry point aplikasi Streamlit
│   └── main_data.csv                           <- Dataset yang sudah dibersihkan (Cleaned Data)
├── PRSA_Data_Wanliu_20130301-20170228.csv      <- Dataset mentah (Raw Data)
├── notebook.ipynb                              <- Jupyter Notebook untuk proses Data Wrangling & EDA
├── README.md                                   <- Dokumentasi cara menjalankan proyek
├── requirements.txt                            <- Daftar library Python yang dibutuhkan
└── url.txt                                     <- Tautan ke dashboard yang sudah di-deploy
```

## 🛠️ Cara Menjalankan Proyek (Local Setup)

Untuk menjalankan dashboard ini di komputer lokal, silakan ikuti langkah-langkah instalasi environment di bawah ini. Anda bisa memilih menggunakan Anaconda atau Terminal/Shell standar.

1. Clone Repositori
   Pertama, clone repositori ini ke komputer lokal Anda:

```bash
git clone [https://github.com/rachmadnanda/SubmissionDataAnalysisDicoding](https://github.com/rachmadnanda/SubmissionDataAnalysisDicoding)
```

2. Setup Environment
   Pilihan A: Menggunakan Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

Pilihan B: Menggunakan Venv (Python Bawaan)

```bash
python -m venv main-ds
main-ds\Scripts\activate     # Untuk pengguna Windows
# source main-ds/bin/activate  # Untuk pengguna Mac/Linux
pip install -r requirements.txt
```

3. Jalankan Aplikasi Streamlit
   Setelah semua library terinstal dengan sukses, jalankan perintah berikut untuk membuka dashboard di browser:

```bash
streamlit run dashboard/app.py
```
