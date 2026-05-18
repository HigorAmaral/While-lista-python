e, d = 0, 0
while True:
    ponto = input().upper()
    if ponto == 'E': e += 1
    elif ponto == 'D': d += 1
    
    if (e >= 21 or d >= 21) and abs(e - d) >= 2:
        break

print("E" if e > d else "D")