# While se repite el bloque de codigo mientra que la condicion sea verdadera True

seguir = True
while seguir:
    print("esto es el while")
    fin = input("Deseas seguir con este while? s/n")
    if fin == 'n':
       seguir = False
       print("Esto se acabo")

# While con else
nombre = "Juana"
while nombre =="Maria":
    print("Hola",nombre)
else:
    print("No es Maria")

x = 0
while x < 100:
    x = x + 1
    print(x)

# Se repite mientas se cumpla en numero de iteracciones definidas dentro del propio FOR,
# Variable range(incio,final(el numero dado menos uno), salto(opcional))

for iteracion in range(1, 21):
    print(iteracion)