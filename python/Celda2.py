vida = 25.0
vida_max = 100.0

pct = (vida / vida_max) * 100

if pct <= 0:
    estado = 'MUERTO'
elif pct <= 25:
    estado = 'CRITICO'
elif pct <= 50:
    estado = 'HERIDO'
elif pct <= 75:
    estado = 'ESTABLE'
else:
    estado = 'SALUDABLE'

print(f'Vida: {vida:.0f}/{vida_max:.0f} ({pct:.0f}%)')
print(f'Estado: {estado}')
clase = 'Mago'
nivel_habilidad = 3

# match (Python 3.10+)
match clase:
    case 'Guerrero': tipo_ataque = 'Espada'
    case 'Mago':     tipo_ataque = 'Hechizo'
    case 'Arquero':  tipo_ataque = 'Flecha'
    case _:          tipo_ataque = 'Puno'

# Condicion compuesta
puede_usar_magia = (
    clase == 'Mago' and nivel_habilidad >= 3
)

if puede_usar_magia:
    print('Bola de fuego!')
else:
    print(f'{tipo_ataque} basico')
