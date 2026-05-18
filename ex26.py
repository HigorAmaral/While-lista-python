massa = float(input())
massa_inicial = massa
tempo = 0

while massa >= 0.0005:
    massa /= 2
    tempo += 50

print(massa_inicial, massa, tempo)