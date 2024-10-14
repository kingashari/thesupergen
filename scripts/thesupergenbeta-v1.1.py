import random

def generate_numbers(jumlah_kombinasi):
  """
  Fungsi untuk menghasilkan kombinasi angka 4D, 3D, dan 2D secara berurutan.

  Args:
    jumlah_kombinasi: Jumlah kombinasi yang ingin dihasilkan.

  Returns:
    List berisi string yang mewakili kombinasi angka.
  """

  kombinasi_4d = []
  for _ in range(jumlah_kombinasi):
    angka_4d = str(random.randint(1000, 9999))
    kombinasi_4d.append(angka_4d)
    kombinasi_3d = angka_4d[1:]
    kombinasi_2d = angka_4d[2:]
    kombinasi_4d.append(kombinasi_3d)
    kombinasi_4d.append(kombinasi_2d)
  return kombinasi_4d

# Meminta input dari pengguna
jumlah_kombinasi = int(input("Masukkan jumlah kombinasi yang ingin dihasilkan: "))

# Menghasilkan kombinasi 4D, 3D, dan 2D
hasil = generate_numbers(jumlah_kombinasi)

# Menampilkan hasil
print("Kombinasi yang akan dihasilkan:", jumlah_kombinasi)
for i in range(0, len(hasil), 3):
  print("4D:", hasil[i])
  print("3D:", hasil[i+1])
  print("2D:", hasil[i+2])