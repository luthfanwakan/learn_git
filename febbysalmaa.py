import numpy as np
number = int(input("Masukkan angka:"))
nilai = [1,1]

for i in range(number-2):
    hasil = nilai[i] + nilai[i+1]
    nilai.append(hasil)

print(nilai)