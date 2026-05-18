contas_encerradas = 0
while True:
    opcao = int(input())
    if opcao == 1:
        nome = input()
        diarias = int(input())
        taxa = 7.5 if diarias < 15 else (6.5 if diarias == 15 else 5.0)
        total = diarias * (50.0 + taxa)
        print(nome, total)
        contas_encerradas += 1
    elif opcao == 2:
        print(contas_encerradas)
    elif opcao == 3:
        break