class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def mostrar_detalles(self):
        print(f"Rectángulo de ancho {self.ancho} y alto {self.alto}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")

    rectangulo = Rectangulo(5, 3)
    rectangulo.mostrar_detalles()

# Clase Cuadrado que hereda de Rectangulo
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # Llama al constructor de Rectangulo con ambos lados iguales
        super().__init__(lado, lado)
    
    def mostrar_detalles(self):
        print(f"Cuadrado de lado {self.alto}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")

# Ejemplo de uso
cuadrado = Cuadrado(4)
cuadrado.mostrar_detalles()