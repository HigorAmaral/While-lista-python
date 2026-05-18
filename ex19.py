n = int(input())
for _ in range(n):
    num = int(input())
    divisores = [i for i in range(1, num + 1) if num % i == 0]
    print(f"Divisores: {divisores} | Qtd: {len(divisores)}")