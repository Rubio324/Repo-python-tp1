fruta0 = "naranja"
fruta1 = "manzana"
fruta2 = "uva"
fruta3 = "frutilla"
fruta4 = "mandarina"

Frutas = [fruta0, fruta1, fruta2, fruta3, fruta4]
print(Frutas)

"""
def imprimir_frutas(Frutas):
    for i in range(len(Frutas)):
        print(f"fruta nro {i} = {Frutas[i]}")

print(imprimir_frutas(Frutas))
"""

def imprimir_frutas(Frutas):
    for i, fruta in enumerate(Frutas):
        print(f"fruta nro {i} = {fruta}")

print(imprimir_frutas(Frutas))