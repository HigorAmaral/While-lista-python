
i = 1
soma_pos = 0
qtd_pos = 0

while i <= 20:
    numero = int(input(f"Digite o {i}º número inteiro: "))

    if numero < 0:
        print(numero)
    else:
        soma_pos = soma_pos + numero
        qtd_pos = qtd_pos + 1

    i = i + 1

if qtd_pos > 0:
    media = soma_pos / qtd_pos
    print(media)
else:
    print("0")

