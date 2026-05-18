preco = 5.0
ingressos = 120
lucro_max = -float('inf')
p_max, ing_max = 0, 0

while preco >= 1.0:
    lucro = (preco * ingressos) - 200
    print(f"Preço: R${preco:.2f} | Ingressos: {ingressos} | Lucro: R${lucro:.2f}")
    if lucro > lucro_max:
        lucro_max, p_max, ing_max = lucro, preco, ingressos
    preco -= 0.5
    ingressos += 26

print(f"Máximo: R${lucro_max:.2f} | Preço: R${p_max:.2f} | Ingressos: {ing_max}")