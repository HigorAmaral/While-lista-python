i = 1
while i <= 15:
    n = int(input(f"Digite o {i}º número inteiro: "))

    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")
        i += 1

