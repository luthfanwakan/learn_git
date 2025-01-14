#Fibonaci 
n = int(input("Masukkan jumlah bilangan Fibonacci yang diinginkan: "))
deret = []
for i in range(n):
    if i == 0:
        deret.append(1)
    elif i == 1:
        deret.append(1)
    else:
        deret.append(deret[i-1]+deret[i-2])

print(*deret, sep=", ")