# Variables del personaje RPG
nombre = 'Gandalf'
nivel = 5
vida = 80.0
vida_maxima = 100.0
mana = 120
esta_vivo = True
clase = 'Guerrero'
puntos_ataque = 15
puntos_defensa = 10

# Verificar tipos
print(type(nombre))   
print(type(nivel))    
print(type(vida))    
print(type(esta_vivo)) 
print(type(mana))
print(f'{nombre} (Nv.{nivel}) - (Vida: {vida}) - (Mana:{mana})')
# Conversiones de tipo
ataque = 15
dano = float(ataque) * 1.5  # cast
msg = 'Dano: ' + str(dano)  # explicito

"""
#* Leer del usuario (input)
nom = input('Nombre: ')
niv = int(input('Nivel: '))
print(f'{nom} Nv.{niv}')

# f-strings (muy utiles)
vida = 87.5
print(f'Vida: {vida:.1f}%')
"""