import math
soma = 0
for i in range(20):
    soma += (100 - i) / math.factorial(i)
print(soma)