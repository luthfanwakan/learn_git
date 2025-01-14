n = 5
a=1
b=1
list = []
for x in range(n):
    list.append(a)
    a,b = b, a + b

print(list)