n = 3

a = 1
b = 1

fib_ = []
for _ in range(n):
    if a != 0 :
        fib_.append(a)
    a, b = b, a + b

print(fib_)
