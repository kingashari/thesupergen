import random

def generate_numbers(jumlah_kombinasi):

    kombinasi = []
    for _ in range(jumlah_kombinasi):
        angka_4d = str(random.randint(1000, 9999))
        angka_3d = angka_4d[1:]
        angka_2d = angka_4d[2:]
        kombinasi.append((angka_4d, angka_3d, angka_2d))
    return kombinasi

# Meminta input dari pengguna
jumlah_kombinasi = int(input("Masukkan jumlah kombinasi yang ingin dihasilkan: "))

# Menghasilkan kombinasi 4D, 3D, dan 2D
hasil = generate_numbers(jumlah_kombinasi)

# Menampilkan hasil dengan format yang diinginkan
print("Kombinasi yang akan dihasilkan:", jumlah_kombinasi)
for i in range(len(hasil)):
    angka_4d_next = hasil[i + 1][0] if i < len(hasil) - 1 else ""
    angka_3d_next = hasil[i + 1][1] if i < len(hasil) - 1 else ""
    angka_2d_next = hasil[i + 1][2] if i < len(hasil) - 1 else ""
    
    # Cetak hasil dalam satu baris untuk setiap kombinasi
    print(f"4D: {hasil[i][0]}*{angka_4d_next}")
    print(f"3D: {hasil[i][1]}*{angka_3d_next}")
    print(f"2D: {hasil[i][2]}*{angka_2d_next}")

    break
