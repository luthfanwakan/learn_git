kotak = []
n = 6

for i in range(n):
    if i < 2:
        kotak.append(1)
    else:
        kotak.append(kotak[i-1] + kotak[i-2])

print(*kotak, sep=" ")