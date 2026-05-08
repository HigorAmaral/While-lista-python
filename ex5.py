soma = 0.0

i = 1
while i <= 20:
    altura = float(input(f"Digite a altura da pessoa {i} em cm: "))
    soma += altura
    i += 1

media = soma / 20
print(f"Média aritmética das alturas: {media} cm")

