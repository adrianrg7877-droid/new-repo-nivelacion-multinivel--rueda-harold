inventario = [
    'Espada de hierro',
    'Pocion de vida',
    'Escudo de madera',
    'Llave dorada'
]

print('=== INVENTARIO ===')
# Con indice
for i, item in enumerate(inventario, 1):
    print(f'{i}. {item}')

# Buscar item especifico
buscar = 'Pocion de vida'
if buscar in inventario:
    print(f'[OK] {buscar} encontrada')
else:
    print(f'[X] {buscar} no disponible')

# Simulacion de combate RPG
vida_hero = 80
vida_enemigo = 60
ronda = 1

while vida_hero > 0 and vida_enemigo > 0:
    # Heroe ataca
    dano_heroe = 15
    vida_enemigo -= dano_heroe

    # Enemigo contraataca
    dano_enemigo = 10
    vida_hero -= dano_enemigo

    print(f'Ronda {ronda}: Hero={vida_hero}'
          f' | Enemigo={vida_enemigo}')
    ronda += 1
    

resultado = 'VICTORIA!' if vida_hero > 0 else 'DERROTA'
print(resultado)
