limite_kg = float(input())
limite_g = limite_kg * 1000
total_g = 0

while True:
    peso = float(input())
    total_g += peso
    print(total_g)
    
    if total_g > limite_g:
        print("Limite excedido!")
        break
        
    if input("informar o peso de mais um peixe: s (SIM)/n(NÃO)? ").lower() == 'n':
        break