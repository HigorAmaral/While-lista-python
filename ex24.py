soma, qtd = 0, 0
continuar = 's'

while continuar == 's':
    idade = int(input())
    if idade > 0:
        soma += idade
        qtd += 1
    continuar = input("deseja digitar mais um valor: s (SIM)/n(NAO)? ").lower()

print(soma / qtd if qtd > 0 else 0)