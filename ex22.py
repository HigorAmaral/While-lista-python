n = int(input())
soma_m, qtd_m, soma_t = 0, 0, 0

for _ in range(n):
    altura = float(input())
    sexo = input().upper()
    soma_t += altura
    if sexo == 'F':
        soma_m += altura
        qtd_m += 1

print(soma_m / qtd_m if qtd_m > 0 else 0)
print(soma_t / n)