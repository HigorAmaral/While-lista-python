n = int(input())
canais = {4: 0, 5: 0, 9: 0, 12: 0}
total_pessoas = 0

for _ in range(n):
    canal = int(input())
    pessoas = int(input())
    if canal in canais:
        canais[canal] += pessoas
        total_pessoas += pessoas

for canal, pessoas in canais.items():
    pct = (pessoas / total_pessoas * 100) if total_pessoas > 0 else 0
    print(f"Canal {canal}: {pct:.2f}%")