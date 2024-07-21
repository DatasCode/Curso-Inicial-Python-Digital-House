# Juego de adivinanza
import os
import random

def limpiar_consola():
    os.system('cls')

limpiar_consola()

numero_secreto = random.randint(1, 100)
adivinado = False
cant_intentos = 0
cant_max_intentos = 5

print("##############################################################")
print("\n###### Bienvenido al juego, adivina el numero secreto #######\n")
print("##############################################################")
while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("\n¡GAME OVER!\n No has podido adivinar en la cantidad de intentos permitido")
        break

    numero = int(input("\nIntroduce un numero del 1 al 99: "))

    if numero == numero_secreto:
        print("¡Felicidades, has adivinado el numero secreto!")
    elif numero < numero_secreto:
        print("El numero secreto, es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cant_intentos +=1

