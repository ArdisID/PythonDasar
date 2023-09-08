# Mulai
nilai_siswa = float(input("Masukkan nilai siswa: ")) # input nilai_siswa
if nilai_siswa >= 75: # input_siswa >= 75
    print("Tuntas") # Tuntas jika nilai_siswa >= 75
else:
    print("Tidak Tuntas") # Tutup jika nilai_siswa < 75
mengulang = input("Apakah Anda ingin mengulang? (Ya/Tidak): ") # input mengulang = 'Ya'
while mengulang == "Ya":
    nilai_siswa = float(input("Masukkan nilai siswa: ")) # input nilai_siswa
    if nilai_siswa >= 75: # input_siswa >= 75
        print("Tuntas") # Tuntas jika nilai_siswa >= 75
    else:
        print("Tidak Tuntas") # Tutup jika nilai_siswa < 75
    mengulang = input("Apakah Anda ingin mengulang? (Ya/Tidak): ") # input mengulang = 'Ya'
# Selesai
