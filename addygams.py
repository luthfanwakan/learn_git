n = int(input("Enter a number: "))
x=[]
for i in range(n):
    if i == 0:
        x.append(1)
    elif i == 1:
        x.append(1)
    else:
        x.append(x[i-1] + x[i-2])

print(*x, sep = ",") 