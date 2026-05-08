n = int(input("Digite a quantidade de atletas (n): "))

i = 1
soma = 0

while i <= n:
    ins = int(input(f"Atleta {i} - inscrição: "))
    altura = float(input(f"Atleta {i} - altura: "))

    soma = soma + altura

    if i == 1:
        maior_alt = altura
        menor_alt = altura
        ins_maior = ins
        ins_menor = ins
    else:
        if altura > maior_alt:
            maior_alt = altura
            ins_maior = ins
        if altura < menor_alt:
            menor_alt = altura
            ins_menor = ins

    i = i + 1

media = soma / n

print(f"Mais alto: {ins_maior} {maior_alt}")
print(f"Mais baixo: {ins_menor} {menor_alt}")
print(f"Média: {media}")

