# Uso de Break, Continue y Pass
# Palabras claves

# USO DE BREAK

contador = 0

while contador < 10:
    print("Contador es igual: ", contador)
    if contador == 9:
        break
    contador +=1

# USO DE CONTINUE

contador = 0

while contador < 25:
    print(contador)
    contador +=1
    if contador == 23:
        continue
    print("Imprimir por cada vuelta")

print(contador)


# Otro ejemplo de continue con CICLO FOR
for i in range(10):
    if i % 2 == 0:
        print(i, "Es par")
    elif i % 3 == 0:
        print(i, "Es impar")


# USO DE PASS
edad = 17

if edad > 18:
    print("Puedes ingresar a trabajar aqui")
elif edad == 18:
    pass
else:
    print("No puedes ingresar a trabajar")
