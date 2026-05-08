soma_pares = 0
soma_impares = 0

n = 1
while n <= 100:
    if n % 2 == 0:
        soma_pares += n
    else:
        soma_impares += n
    n += 1

print(f"Soma dos pares (1..100): {soma_pares}")
print(f"Soma dos ímpares (1..100): {soma_impares}")

