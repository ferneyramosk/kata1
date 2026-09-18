#comentarios en una sola linea

"""
Comwentarios en virias lineas
esto si mola
"""

'''
otra froma de comentar
en varias lineas
'''

#salida de informacion
print("salida de informacion")

#Entrada de informacion
nombre = input("Igrese su nombre") #un imput captura el dato ingresado por terminal y siempre
                                   #lo devuelve en formato str

print("Su nombre es:",nombre,nombre)
#print(f"Su nombre es:",nombre es un cliente)

#tipos de variables en python
#str "@dfjsdfjsdlñfjkslñ¿'" permite escribir todo lo que esta en el teclado, con comilla simple y doble

#int 100 -> entero
#float -> decimal
#bool -> True o False
variable = 1000
print(type(variable)) # Da el tipo de variable
# Variables sensibles a mayusculas y minusculas.
# variable1 = "Carlos"
# vARIABLE1 = "Ivan"        ----> las tres son variables distintas
# Variable1="Jose" 
#print(variable1)
#print(vARAIBLE1)
#print(Variable1)

nombre = None,                  # Variable vacia esperando ejecucion

def nombra():                   # Funcion esperando un retorno
    pass

# Las variables de python son flexible.
"""
nombre = "Rolando"
print(nombre)
nombre = True
print(nombre)                ----> Ojo no se puede replicar la variable
nombre = 100
print(nombre)

"""

def nombrar(num:str)->bool:         # Lo que va a salir en este caso un boleano
    return

# Reglas de nombres de variables
# Nombre de variables t funciones van en minusculas
# Nombre de class con la primera letra en Mayuscula.
# Nombre de variables de tipo constante ejemplo: VALOR_PI = 3.142355; el VALOR_PI debe estar en mayuscula
# Declaracion de variables

# No se puede hacer
# 1) Numero entre una letra, en nombre de variable
# 2) 10valor = "Ana"
# 3) Espacios entre nombre de variable
# 4) Ejemplo: cuenta bancaria = 1000 -> esta separada las letras de la variable
# 5) Ejemplo: cuenta_bancaria = 1000 -> Asi se debe hacer

# Lo que si se puede hacer
# nombre10 = "Ana"
# Snake case o camel case
cuenta_bancaria_conjunta = 1000
CuentaCorrienteCerrado = 1000
"""
numero1 = "100"
numero2 = 50
suma = numero1 + numero2       ---> Error, las variables son distintas; SNR + INT
print("la suma es",suma)
"""

#Casting o casteo
numero1 = "100" 
numero2 = 50
suma = int(numero1) + numero2     # Se realiza el casteo para convertir un str a un int y realizar la suma
print ("la suma es",suma)

# Se puede hacer el casting o conversion de tipos de todas variables
# str(aqui el valor), bool(aqui el valor), floar(aqui el valor)
