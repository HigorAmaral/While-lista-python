menor = None
maior = None

numero = int(input("Digite um número inteiro positivo (0 para terminar): "))
while numero != 0:
    if numero < 0:
        print("Valor ignorado (deveria ser positivo).")
    else:
        if menor is None or numero < menor:
            menor = numero
        if maior is None or numero > maior:
            maior = numero

    numero = int(input("Digite um número inteiro positivo (0 para terminar): "))

if menor is None:
    print("Nenhum valor positivo foi informado.")
else:
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")

