n = int(input("Masukkan angka: "))
a = 1
b = 1

print("Deret Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b