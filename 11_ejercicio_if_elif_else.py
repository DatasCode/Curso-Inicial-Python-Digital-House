# Ejercicio Ingreso internacion

import os

def limpiar_consola():
    os.system('cls')

limpiar_consola()

visa = False
passport = True
print()
if visa and passport:
    print("Puedes ingresar al pais de destino")
elif passport and not visa:
    print("No puedes ingresar a paises que requieran visa")
else:
    print("No puedes ingresar, debes conseguir la documetacion requerida")

print()



print("\nSiguiente ejercicio: \n")
print()

edad = 61
if edad < 18 or edad > 60:
    if edad < 18:
        print("No puedes ingresar a la disco, por ser menor de edad\n")
    else:
        print("Por cuestiones de seguridad, no se permite mayores a 60\n")
elif edad >= 18 and edad <= 60:
    print("Puedes ingresar a la disco\n")