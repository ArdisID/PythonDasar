# Mulai
nama = input("Masukkan nama: ") # input nama
gaji_pokok = float(input("Masukkan gaji pokok: ")) # input gaji pokok
if gaji_pokok <= 1000000: # gaji pokok <= 1000000
    pajak = 0.1 # pajak = 0.1
else:
    pajak = 0.2 # pajak = 0.2
tunjangan = 0.1 * gaji_pokok # tunjangan = 0.1 * gaji pokok
gaji_bersih = gaji_pokok - (pajak * gaji_pokok) + tunjangan # gaji bersih = gaji pokok - (pajak * gaji pokok) + tunjangan
print(f"Nama: {nama}") # output nama
print(f"Gaji Bersih: {gaji_bersih}") # output gaji bersih
# Selesai