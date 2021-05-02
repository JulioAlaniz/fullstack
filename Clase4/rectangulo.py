#Escribe una clase de Python llamada Rectangulo que se define por una longitud 
# y un ancho y un método que calculará el área de un rectángulo.

# **************** Import ***************
import os

# **************** Funciones ***************
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
        
class Rectangulo:
    def __init__(self, ancho, longitud):
        self.ancho = float(input('ingrese ancho\n'))        
        self.longitud = float(input('ingrese largo\n'))

    def area(self):
        return (self.ancho) * (self.longitud)


borrarPantalla()

rec = Rectangulo(0,0)
print('\nel area del rectangulo es: ',rec.area())

# *********************** Modificaciones - Mejoras **********************

# agregar un try para evitar errores en la entrada de datos junto con un for 
# para volver a intentarlo. 

