# Air Quality Dashboard

Selamat datang di proyek **Air Quality Analysis Dashboard**!
Proyek ini merupakan submission untuk kelas **Belajar Analisis Data dengan Python** dari Dicoding. Dashboard interaktif ini dibuat menggunakan Streamlit untuk mengeksplorasi dan menganalisis tren kualitas udara di Stasiun Wanliu.

## Fitur Dashboard

- **Filter Tahun Interaktif:** Menyesuaikan rentang waktu analisis sesuai kebutuhan.
- **Tren PM2.5 Bulanan:** Visualisasi pergerakan polusi udara secara _time-series_.
- **Analisis Korelasi:** Memahami dampak Suhu (TEMP) dan Kecepatan Angin (WSPM) terhadap polusi.
- **Kategori Kualitas Udara (AQI):** Pengelompokan level polusi melalui teknik _Binning_.

---

## Setup Environment - Anaconda

Jika Anda menggunakan distribusi Anaconda, jalankan urutan perintah berikut di Anaconda Prompt:

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

Jika Anda menggunakan Terminal atau Command Prompt standar dengan pipenv, jalankan urutan perintah berikut:

Jika Anda menggunakan distribusi Anaconda, jalankan urutan perintah berikut di Anaconda Prompt:

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run streamlit app

Setelah environment siap dan seluruh library terinstal, jalankan aplikasi Streamlit menggunakan perintah berikut:

```bash
streamlit run dashboard/app.py
```

(Catatan: Pastikan Anda menjalankan perintah ini dari root folder proyek Anda)
