s = 0
for i in range(51):
    termo = 1 / ((2 * i + 1) ** 3)
    if i % 2 == 1:
        s -= termo
    else:
        s += termo
pi = (s * 32) ** (1/3)
print(pi)