xp = 0
nivel = 1
xp_necesario = 100
batallas = [20, 35, 15, 40, 30]

for xp_ganado in batallas:
    xp += xp_ganado
    
    if xp >= xp_necesario:
        nivel += 1
        xp -= xp_necesario
        print(f'Nivel {nivel}')