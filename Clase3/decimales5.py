#Escribe un programa Python que acepte 5 números decimales del usuario.
#**********importar**********
import math
#**********variables*********
i = 0
listaDecimal = []
#**********aplicacion********
while i < 5:
    try:
        num=float(input("ingrese variable : "))
        decimal, entera = math.modf(num)            #identifica la parte entera y decimal de la varialble num
        if decimal != 0:                            #filtra los numeros decimales
            listaDecimal.append(num)                #agrega los num a listaDecimal[] 
            i += 1
        else:
            print("dato no válido, debe ser un numero decimal")
    except:
        print("dato no valido")
        
print("La lista 'listaDecimal' esta formada por: ", listaDecimal)

