vida_enemigo = 40
ataque = 35
nivel_jugador = 6

# Bonificación según el nivel
if nivel_jugador >= 5:
    bonificacion = 10
else:
    bonificacion = 0

# Cálculo del daño total
dano_total = ataque + bonificacion

# Vida restante del enemigo
vida_restante = vida_enemigo - dano_total

print(f'Daño total: {dano_total}')
print(f'Vida restante del enemigo: {vida_restante}')

# Estado del enemigo
if vida_restante <= 0:
    print('Enemigo derrotado! +50 XP')
elif vida_restante <= 20:
    print('Enemigo en estado critico')
else:
    print(f'Enemigo resiste. Vida restante: {vida_restante}')