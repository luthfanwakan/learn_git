n = 10 
list_fibo = [1, 1]  
for i in range(2, n):  
    list_fibo.append(list_fibo[-1] + list_fibo[-2])  


list_fibo[:n] 
  
result = list_fibo[:n]
  
print(result)