#Dada una lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]), iterarla y
#mostrar números divisibles por cinco, y si encuentra un número mayor que 150, detenga la iteración
#del bucle.


#**********importar**********


#**********variables*********
lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
dato = 0
i = 0
#**********aplicacion********
for i in range(len(lista1)):
    dato = lista1[i]
    i += 1
#    print(dato)
    if dato >= 150:
        break
    elif dato%5 == 0 or dato%5 == 5:
        print(dato)

   