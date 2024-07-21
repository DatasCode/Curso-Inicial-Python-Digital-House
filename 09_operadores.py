# Operadores
# Son simbolos o conjuntos que realizan una operacion especifica

# Tipos de operadores:
# Aritmeticos, de comparacion, de asignacion, logicos, de pertenencia, de identidad

################################################
############ OPERADORES ARITMETICOS  ###########
################################################

# + Suma
# - Resta
# * Multiplicacion
# / division
# // dividir entero
# % resto o modulo
# ** exponenciacion
"""
print("\nOperadores Aritmeticos\n")

a = 3
b = 2
c = a / b
d = a // b
e = a % b

f = a ** b
print(c)
print(d)
print(e)
print(f)

################################################
########### OPERADORES DE ASIGNACION ###########
################################################
print("\nOperadores de Asignacion\n")

x = 5
sumatorio = 4

x += sumatorio
x += sumatorio
x += sumatorio
x += sumatorio
x += sumatorio
x += sumatorio

print("x =", x)

x -= sumatorio

print("x2 =", x)

x *= sumatorio

print("x3 =", x)

x /= sumatorio

print("x4 =", x)

x //= sumatorio

print("x5 =", x)

x %= sumatorio

print("x6 =", x)

x **= sumatorio

print("x7 =", x)


################################################
########## OPERADORES DE COMPARACION ###########
################################################
print("\nOperadores de Comparacion\n")

x = 5
z = 6

r = x > 3 & x < 5
r2 = x == z or x != z
r3 = (x + z < 10)
print(r)
print(r2)
print(r3)


################################################
############ OPERADORES DE IDENTIDAD ###########
################################################
print("\nOperadores de Identidad\n")

a = 5
b = 5

r = a is not b
print(r)

c = 4
d = 3
r = not c == d
print(r)

"""

################################################
########## OPERADORES DE PERTENENCIA ###########
################################################
print("\nOperadores de Pertenencia\n")

a = "En texto pondremos algunas tecnologia: Python, R, DJango y TensorFlow"

print("DJango" in a)
print("DJango" not in a)

x = a.upper()

print("TENSORFLOW" in x)
print(x)