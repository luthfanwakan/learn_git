temp = []
n = 5

for i in range(n):
    if i < 2:
        temp.append(1)
    else:
        temp.append(temp[i-1] + temp[i-2])

print(temp)