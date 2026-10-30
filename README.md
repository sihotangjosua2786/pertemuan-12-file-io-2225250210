Pertemuan 12 - File I/O dan Error Handling
Nama : Josua Evanno M A Sihotang NIM : 2225250210 
Kelas: 3B

Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python.

Format File Input
NIM,nilai

Contoh:

A001,85 A002,78 A003,92

Cara Menjalankan
python3 tugas/rekap_nilai_file.py

Error yang Ditangani
FileNotFoundError
ValueError
Test Case
Kasus 1 Normal
Input: A001,85 A002,78

Hasil: Rekap berhasil dibuat.

Status: Berhasil

Kasus 2 File Hilang
Input: nilai.txt dihapus

Hasil: File tidak ditemukan.

Status: Berhasil

Kasus 3 Nilai Tidak Valid
Input: A004,abc

Hasil: Baris dilewati

Status: Berhasil

Kasus 4 Baris Kosong
Input: (baris kosong)

Hasil: Dilewati

Status: Berhasil

Kasus 5 Batas Lulus
Input: A007,60

Hasil: Dihitung lulus

Status: Berhasil

Refleksi
Saya menemukan error ValueError saat data nilai berisi teks. Program menggunakan try-except sehingga data lain tetap dapat diproses dan rekap tetap dibuat.