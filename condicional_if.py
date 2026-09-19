a = 10
b = 5

print(a < b)   # False mayor que
print(a > b)   # True menor que
print(a !=b)   # True distinto que
print(a == b)  # Falso igual que

"""
Condicional, es un estrutura la cual ingresa al bloque de codigo mientras su
condicion sea verdadera
"""

#if True:        # imprime 
#    print("'a' es mayor a 'b'")

#if False:
#    print("'a' es mayor a 'b'")


# Sino else ingresa si no es verdadera la primera condicion if
"""
if a > b:
    print("'a' es mayor a 'b'")
else:
    print("'a' es menor o igual a 'b'")
"""
"""
dia = "viernes"

if dia == "Martes":
    print("es martes")
elif dia == "miercoles":
    print("es miercoles")
elif dia == "jueves":
    print("es jueves")
elif dia == "viernes":
    print("es viernes")
else:
    print("no se sabe que dia")
"""

usuario = None
password = None

usuario = input("Igrese su usuaio: ")
password = input("Ingrese su password: ")

# rolando@gmail y rolando12345 credenciales correctas

#Operadores de union and, or, not

if usuario == "rolando@gmail.com" and password == "rolando12345":
    print("Bienvenido al sistema")

else:
    print("Credenciales no validos")