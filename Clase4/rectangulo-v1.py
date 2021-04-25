#Escribe una clase de Python llamada Rectangulo que se define por una longitud 
# y un ancho y un método que calculará el área de un rectángulo.

class Rectangulo:
    def __init__(self, ancho, longitud):
        self.ancho = ancho
        self.longitud = longitud

    def area(self):
        return f (self.ancho) * (self.longitud)

    def __str__(self):
        return f (self.ancho) * (self.longitud)

miRectangulo = Rectangulo (ancho, longitud)
ancho = input("ingrese el ancho")
longitud = input("ingerse largo")

print(area)
