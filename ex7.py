tinta = float(input("Digite a quantidade inicial de tinta (ex.: 1.0): "))

while tinta > 0:
    print("Enquanto tem tinta a caneta escreve...")
    tinta = tinta * (1 - 0.02)

print("Fim da tinta.")

