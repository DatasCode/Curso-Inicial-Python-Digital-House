# Ejemplo de Try, except y finally

# Control de la division por 0, que genera error

a = 5
b = 0

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("No se puede dividir por 0")
finally:
    c = 0

print(c)