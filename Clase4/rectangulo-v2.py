#Escribe una clase de Python llamada Rectangulo que se define por una longitud 
# y un ancho y un método que calculará el área de un rectángulo.
class Rectangulo():
    largo=0
    ancho=0

    def area(self):
        largo =float(input("ingrese largo\n"))
        ancho =float(input("ingrese ancho\n"))
        print ("el area del rectangulo es: ",largo*ancho,"cm2")

  
rec = Rectangulo()
rec.area()
