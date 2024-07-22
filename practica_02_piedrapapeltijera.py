# Juego de Piedra, Papel, Tijera
# se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowercase de tal forma de comparar minuscula con minuscula
# Mas de 1 turno con el bucle while

from math import fabs
import os
def limpiar_consola():
    os.system('cls')

limpiar_consola()


nombre1 = input("¿Como se llamará el jugador 1?: ")
nombre2 = input("¿Como se llamará el jugador 2?: ")

while True:
    jugador1 = input("¡Hola " + nombre1 + "! ¿Que eliges? ¿Piedra, Papel o tijeras?: ")
    jugador2 = input("¡Hola " + nombre2 + "! ¿Que eliges? ¿Piedra, Papel o tijeras?: ")

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"


    if jugador1 == jugador2:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado:", nombre1)
    else:
        print("Ha ganado:", nombre2)

    respuesta = input(" \n¿Desea seguir jugando (s/n?: ")
    if respuesta.lower() != 's':
        print("Hasta pronto...")
        break
