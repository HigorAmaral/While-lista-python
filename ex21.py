nomes_18 = []
qtd_acima_20 = 0

for _ in range(50):
    nome = input()
    idade = int(input())
    if idade == 18:
        nomes_18.append(nome)
    if idade > 20:
        qtd_acima_20 += 1

print(nomes_18)
print(qtd_acima_20)