p_r = float(input())
p_c = float(input())
p_i = float(input())
n = int(input())

tot_r, tot_c, tot_i, total_geral = 0, 0, 0, 0

for _ in range(n):
    id_conf = input()
    kwh = float(input())
    tipo = input().upper()

    total_geral += kwh
    if tipo == "R":
        tot_r += kwh
        pago = kwh * p_r
    elif tipo == "C":
        tot_c += kwh
        pago = kwh * p_c
    elif tipo == "I":
        tot_i += kwh
        pago = kwh * p_i

    print(id_conf, pago)

print(tot_r, tot_c, tot_i)
print(total_geral / n)
