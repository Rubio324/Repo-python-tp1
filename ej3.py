PI = 3.14159
def calcular_propiedades_circulo(radio):

    area = PI * radio ** 2
    circunferencia = 2 * PI * radio
    diametro = 2 * radio
    return area, circunferencia, diametro

# usando la función con una tupla como salida
resultado = calcular_propiedades_circulo(5)
print(resultado)

# desempaquetando los valores retornados uno a uno
a, c, d = calcular_propiedades_circulo(5)
print(f"Área: {a}, Circunferencia: {c}, Diámetro: {d}")