import streamlit as st

# Judul aplikasi
st.title("Kalkulator Angka Kecukupan Gizi (AKG)")

# Memasukkan data pengguna
usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25, step=1)
jenis_kelamin = st.radio("Jenis Kelamin", ("Laki-laki", "Perempuan"))
berat_badan = st.number_input("Berat Badan (kg)", min_value=10.0, max_value=200.0, value=70.0, step=0.1)
tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=50.0, max_value=250.0, value=175.0, step=0.1)
aktivitas = st.radio("Tingkat Aktivitas", ("Rendah", "Sedang", "Tinggi"))

# Fungsi untuk menghitung kebutuhan kalori
def hitung_kalori(usia, jenis_kelamin, berat_badan, tinggi_badan, aktivitas):
    # Menggunakan rumus Mifflin-St Jeor
    if jenis_kelamin == "Laki-laki":
        bmr = 10 * berat_badan + 6.25 * tinggi_badan - 5 * usia + 5
    else:
        bmr = 10 * berat_badan + 6.25 * tinggi_badan - 5 * usia - 161
    
    # Faktor aktivitas
    if aktivitas == "Rendah":
        kebutuhan_kalori = bmr * 1.2
    elif aktivitas == "Sedang":
        kebutuhan_kalori = bmr * 1.55
    else:
        kebutuhan_kalori = bmr * 1.725
    
    return kebutuhan_kalori

# Tombol untuk menghitung
if st.button("Hitung Kebutuhan Kalori"):
    hasil = hitung_kalori(usia, jenis_kelamin, berat_badan, tinggi_badan, aktivitas)
    st.success(f"Kebutuhan kalori harian Anda adalah {hasil:.2f} kalori.")