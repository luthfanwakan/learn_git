n=8
deret_fibonacci=[]
for i in range(n):
    if i<2 :
        deret_fibonacci.append(1)
    else :
        deret_fibonacci.append(deret_fibonacci[i-1]+deret_fibonacci[i-2])
print(deret_fibonacci)

