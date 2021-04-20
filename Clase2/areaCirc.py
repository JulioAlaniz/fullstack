#calculo del area de un circulo v1
#julio alaniz
#**********importar**********
import math
#**********variables*********
r = float(input("ingrese el radio de la circunsfeencia en cm:\n"))
#**********aplicacion********
area = (r**2) * (math.pi)
print("el area es: " + str(f"{area:.2f}") + "cm2")