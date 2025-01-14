n = 8
a, b = 1, 1

list=[]
for i in range(n):
    list.append(a)
    a, b = b ,a + b
    print(list)