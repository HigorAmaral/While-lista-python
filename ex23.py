while True:
    nome = input()
    if nome == "ULTIMO":
        break
    endereco = input()
    valor = float(input())
    desc = 0.20 if valor > 500 else 0.15
    print(valor * (1 - desc))