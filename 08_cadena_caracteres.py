"""
txt = "Hola Mundo"

print(txt[0])
print(txt[1])
print(txt[2])
print(txt[3])
print(txt[4])
print(txt[5])
print(txt[6])
print(txt[7])
print(txt[8])
print(txt[9])

print()

print(len(txt))

comentario = "lorem ipsum trota latin mailgib ochoa tomba"

print("ipsum" in comentario)
print("Juan" not in comentario)
print("Juan"  in comentario)




print("###############################################################")
print("Seguimos trabajando con cadena de caracteres parte 2- SLICING")
print("###############################################################\n")

txt ="Seguimos trabajando con cadena de caracteres"

print(txt[0:19])
print(txt[20:])
print(txt[-5:-10])

# cambiar a mayusculas, minusculas, capital
print(txt.capitalize())
print(txt.lower())
print(txt.upper())


# Correccion de espacios
txt = "     uy, me olvide y puse      espacios de mas     "
print(txt)

txtimportante = "Clave   "

print("Espacios corregidos")
print(txtimportante.strip())
print(len(txtimportante))



print("###############################################################")
print("Seguimos trabajando con cadena de caracteres parte 3- CONCATENAR")
print("###############################################################\n")


horas = 10
txt = "El contenido de este de este curso va  durar {} horas"

print(txt.format(horas))

horas = 20
clases = 10
txt = "Este curso tiene {0} clases y dura {1} horas"
print(txt.format(horas, clases))

txt = "Una de las mejores peliculas es \"GAME OF THRONES\""
print(txt)

txt = "mi curso esta en la carpeta c:\\cursos\\python"
print(txt)

"""


print("###############################################################")
print("Seguimos trabajando con cadena de caracteres parte 4- METODOS") 
print("###############################################################\n")


txt ="Esto es un parrafo para hacer pruebas"

print(txt.center(20))