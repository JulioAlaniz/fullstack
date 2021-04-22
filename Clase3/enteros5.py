#enteros5 v13
#Escribe un programa Python que reciba 5 números enteros del usuario y los guarde en una lista.
#luego recorrer la lista y mostrar los numeros por pantalla
#**********importar**********
import math
#**********variables*********
i = 0
listaEntero = []
#**********aplicacion********
while i < 5:
    try:
        num=int(input("ingrese variable : "))
        decimal, entera = math.modf(num)    #identifica la parte entera y decimal de la varialble num
        if decimal == 0:                    #filtra los numeros enteros
            listaEntero.append(num)         #agrega los num a listaEntero[]
            i += 1
        else:
            print("dato no válido, debe ser un numero entero")
    except:
        print("dato no valido")
print()
print("La lista 'listaEntero' esta formada por: \n")
for i in range(len(listaEntero)):
    print("indice: ", i," valor: ", listaEntero[i]) # Muestra el numero indice y valor de la lista