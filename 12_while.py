# Bucle while
# significa, mientras se cumpla una condicion
import os
def limpiar_consola():
    os.system('cls')

limpiar_consola()
contador = 0

#while contador < 5:
#    print("El contador es: ", contador)
#    contador +=1


contador = 0
limite = 5
sumatoria = 0

while contador <= limite:
    sumatoria += contador
    contador += 1

print("La suma de los numeros hasta: ", limite, "es", sumatoria)