import numpy as np
angka = int(input("Masukan Jumlah Pasukan Anda : "))
nilai = [1,1]

for i in list(range(angka-2)):
    kambing = i
    kucing = nilai[i] + nilai[i+1]
    nilai.append(kucing)
    

 print(nilai)   