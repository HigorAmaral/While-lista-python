n = int(input())
odo_anterior = float(input())
total_litros = 0
km_inicial = odo_anterior

for _ in range(n - 1):
    odo_atual = float(input())
    litros = float(input())
    print((odo_atual - odo_anterior) / litros)
    total_litros += litros
    odo_anterior = odo_atual

print((odo_anterior - km_inicial) / total_litros)