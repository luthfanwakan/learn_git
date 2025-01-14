n = int(input("Masukkan jumlah data: "))
sequence = []
a, b = 1, 1
while len(sequence) < n:
    sequence.append(a)
    a, b = b, a + b

print(sequence)