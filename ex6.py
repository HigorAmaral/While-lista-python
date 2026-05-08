numero = int(input("Digite a quantidade de números (n): "))

negativos_count = 0

i = 1
while i <= numero:
    inteiro = int(input(f"Digite o {i}º número inteiro: "))
    if inteiro < 0:
        negativos_count += 1
    i += 1

print(f"Quantidade de números negativos: {negativos_count}")

