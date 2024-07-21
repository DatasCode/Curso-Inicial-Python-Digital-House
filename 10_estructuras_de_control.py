#############################################################
############## ESTRUCTURAS DE CONTROL #######################
#############################################################

"""

a = 3
b = 6

if a > b:
    print("A",a , " es Mayor que B", b)
print("B",b , " es Mayor que A", a) 


"""

import os

# Limpiar consola, antes de ejecutarse
def limpiar_consola():
     os.system('cls')

# Llamar a funcion limpiar
limpiar_consola()

print("PRUEBA DE SENTENCIA IF ELIF ELSE")

while True:
    
    a = int( input("\nIngrese un numero: \n") )
    b = int( input("\nIngrese otro numero: \n") )

    if a > b:
        print("A",a , " es Mayor que B", b)
    elif a == b:
            print("B",b , " es igual que A", a) 
    else:
        print("B",b , " es mayor que A", a)
    
    respuesta = input(" \n¿Desea realizar otra comparacion (s/n?: ")
    if respuesta.lower() != 's':
        break


