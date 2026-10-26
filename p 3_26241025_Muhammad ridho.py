# ================================
# Program Identitas Mahasiswa
# Nama : muhammad ridho
# NIM  : 26241025
# Program Studi :Pendidikan Teknologi Informasi
# Mata Kuliah : Pemrograman Dasar
# ================================

print("================================")
print("     IDENTITAS MAHASISWA")
print("================================")

# Input data dari pengguna
nama = input("Masukkan Nama            : ")
nim = int(input("Masukkan NIM             : "))
prodi = input("Masukkan Program Studi   : ")
dua_digit_nim = int(input("Masukkan 2 Digit Terakhir NIM : "))

# Menampilkan hasil
print()
print("================================")
print("        HASIL PROGRAM")
print("================================")
print()

print("Nama          :", nama)
print("NIM           :", nim)
print("Prodi         :", prodi)
print("2 Digit NIM   :", dua_digit_nim)

print()
print("Tipe Data Nama:", type(nama))
print("Tipe Data NIM :", type(nim))
print("Tipe Data Prodi :", type(prodi))
print("Tipe Data 2 Digit NIM :", type(dua_digit_nim))
print("================================")