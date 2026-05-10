# Funciones RPG 

def calcular_dano(ataque: int, defensa: int) -> int: 
    '''Retorna el dano real (minimo 1)''' 
    dano = ataque - defensa 
    return dano if dano > 0 else 1 

def aplicar_curacion( 
    vida: float, cur: float, max_vida: float) -> float: 
    '''Cura sin pasar el maximo''' 
    nueva = vida + cur 
    return min(nueva, max_vida) 

def mostrar_estado( 
    nombre: str, vida: float, nivel: int): 
    '''Imprime el estado del personaje''' 
    print(f'{nombre} [Nv{nivel}] HP: {vida:.0f}') 

def subir_nivel(xp_actual: int, xp_necesario: int, nivel_actual: int) -> int:     #implementacion de la funcion 
    '''Sube de nivel si el xp actual alcanza el necesario'''
    if xp_actual >= xp_necesario:
        nivel_actual += 1
        xp_actual = 0
        print(f'¡Nivel alcanzado! Ahora eres nivel {nivel_actual}')
    return nivel_actual

# Prueba original
d = calcular_dano(20, 8) 
print(f'Dano: {d}') 
v = aplicar_curacion(40, 80, 100) 
mostrar_estado('Frodo', v, 3)

# Prueba subir_nivel
print(f'\nNivel resultado: {subir_nivel(110, 100, 3)}')  # -> 4
print(f'Nivel resultado: {subir_nivel(80, 100, 3)}')    # -> 3