class Rectangulo:
    def __init__(self, ancho, alto):
        # Inicializa los atributos de ancho y alto
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto
    def perimetro(self):
        return self.ancho*2 + self.alto*2
    
    def mostrar_detalles(self):
        # Mostrar detalles por pantalla usando print()
        print(f"Rectángulo de ancho {self.ancho} y alto {self.alto}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")
    
    # Ejemplo de uso
rectangulo = Rectangulo(5, 3)
rectangulo.mostrar_detalles()