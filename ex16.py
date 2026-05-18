import math
x = float(input())
soma = 0
for i in range(30):
    soma += (x ** i) / math.factorial(i)
print(soma)