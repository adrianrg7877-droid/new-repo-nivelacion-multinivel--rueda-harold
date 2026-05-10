

def calcular_dano(ataque: int, defensa: int) -> int:
    '''Retorna el daño real (mínimo 1)'''
    dano = ataque - defensa
    return dano if dano > 0 else 1

def aplicar_curacion(vida: float, cur: float, max_vida: float) -> float:
    '''Cura sin pasar el máximo'''
    return min(vida + cur, max_vida)

def mostrar_estado(nombre: str, vida: float, nivel: int = 0):
    '''Imprime el estado del personaje'''
    if nivel:
        print(f'  {nombre} [Nv{nivel}] HP: {vida:.0f}')
    else:
        print(f'  {nombre} HP: {vida:.0f}')

def combatir(vida_heroe: float, ataque_heroe: int, def_heroe: int,
             vida_enemigo: float, ataque_enemigo: int,
             nombre_heroe: str, nombre_enemigo: str, nivel_heroe: int) -> float:
    '''
    Simula el combate turno a turno entre héroe y enemigo.
    Retorna la vida restante del héroe (0 si murió).
    '''
    print(f'\n  ⚔️  {nombre_heroe} VS {nombre_enemigo}')
    print(f'  {"-"*30}')
    turno = 1

    while vida_heroe > 0 and vida_enemigo > 0:
        print(f'\n  [Turno {turno}]')

        # Héroe ataca
        dano_heroe = calcular_dano(ataque_heroe, 0)  # enemigos sin defensa
        vida_enemigo -= dano_heroe
        vida_enemigo = max(vida_enemigo, 0)
        print(f'  {nombre_heroe} ataca por {dano_heroe} de daño.')
        print(f'  {nombre_enemigo} HP: {vida_enemigo:.0f}')

        if vida_enemigo <= 0:
            print(f'\n  ✅ {nombre_enemigo} ha sido derrotado!')
            break

        # Enemigo contraataca
        dano_enemigo = calcular_dano(ataque_enemigo, def_heroe)
        vida_heroe -= dano_enemigo
        vida_heroe = max(vida_heroe, 0)
        print(f'  {nombre_enemigo} contraataca por {dano_enemigo} de daño.')
        print(f'  {nombre_heroe} HP: {vida_heroe:.0f}')

        turno += 1

    return vida_heroe


# 1. VARIABLES DEL HÉROE Y ENEMIGOS

# Héroe
heroe = {
    'nombre':   'Guerrero',
    'nivel':    2,
    'vida':     80,
    'vida_max': 80,
    'ataque':   18,
    'defensa':  8
}

# Lista de enemigos
enemigos = [
    {'nombre': 'Goblin', 'vida': 40,  'ataque': 8},
    {'nombre': 'Orco',   'vida': 70,  'ataque': 14},
    {'nombre': 'Dragon', 'vida': 120, 'ataque': 25},
]

# INICIO DEL SIMULADOR

print('=' * 45)
print('       ⚔️   SIMULADOR DE COMBATE RPG   ⚔️')
print('=' * 45)
print(f"\n🧙 Héroe: {heroe['nombre']} [Nv{heroe['nivel']}]")
print(f"   HP: {heroe['vida']} | ATK: {heroe['ataque']} | DEF: {heroe['defensa']}")
print(f"\n👾 Enemigos: {', '.join(e['nombre'] for e in enemigos)}")

enemigos_derrotados = 0

# 3. CICLO QUE RECORRE LOS 3 ENEMIGOS

for i, enemigo in enumerate(enemigos):
    print(f'\n{"=" * 45}')
    print(f'  COMBATE {i+1}/3: vs {enemigo["nombre"].upper()}')
    print(f'{"=" * 45}')

    vida_restante = combatir(
        vida_heroe      = heroe['vida'],
        ataque_heroe    = heroe['ataque'],
        def_heroe       = heroe['defensa'],
        vida_enemigo    = enemigo['vida'],
        ataque_enemigo  = enemigo['ataque'],
        nombre_heroe    = heroe['nombre'],
        nombre_enemigo  = enemigo['nombre'],
        nivel_heroe     = heroe['nivel']
    )

    # 4. CONDICIONALES: ¿héroe muerto o vivo?

    heroe['vida'] = vida_restante

    if heroe['vida'] <= 0:
        print(f"\n  💀 {heroe['nombre']} ha caído en combate...")
        print(f'{"=" * 45}')
        print(f'\n❌ GAME OVER')
        break
    else:
        enemigos_derrotados += 1

        # Curación post-combate (si no es el último enemigo)
        if i < len(enemigos) - 1:
            vida_antes = heroe['vida']
            heroe['vida'] = aplicar_curacion(heroe['vida'], 20, heroe['vida_max'])
            curado = heroe['vida'] - vida_antes
            print(f"\n  💊 El héroe descansa y recupera {curado:.0f} HP.")
            mostrar_estado(heroe['nombre'], heroe['vida'], heroe['nivel'])


# 5. RESULTADO FINAL

print(f'\n{"=" * 45}')
print('           📊 RESULTADO FINAL')
print(f'{"=" * 45}')
print(f"  👾 Enemigos derrotados : {enemigos_derrotados}/3")
print(f"  ❤️  Vida restante       : {heroe['vida']:.0f}/{heroe['vida_max']}")

if enemigos_derrotados == 3:
    print('\n  🏆 ¡VICTORIA! ¡El héroe venció a todos!')
else:
    print(f"\n  💀 El héroe cayó tras {enemigos_derrotados} combate(s).")
print('=' * 45)