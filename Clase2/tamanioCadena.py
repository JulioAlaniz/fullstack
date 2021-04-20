#tamaño de cadena y busqueda de caracteres v1
#julio alaniz
#**********importar**********
#
#**********variables*********
cadena = (input("ingrese una cadena de caracteres:\n"))
letra = (input("ingrese la letra a buscar:\n"))
letra1 = (input("ingrese la segunda letra a buscar:\n"))
#**********aplicacion********
print(cadena, "\n\n")
print("la cantidad de caracteres es: ",len(cadena))
print("la cantidad de letra", letra, "es: ", cadena.count(letra))
print("la cantidad de la segunda letra", letra1, "es: ", cadena.count(letra1))
