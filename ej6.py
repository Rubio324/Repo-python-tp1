

"""
notasJuan = [10, 7, 5, 2]
notasPedro = [4, 7, 5, 6]


DiccionarioPedro= dict( nombre = "Pedro", notas = notasPedro)
DiccionarioJuan= dict( nombre = "Juan", notas = notasJuan)


# Calcular el promedio de las notas de cada estudiante
promedioPedro = sum(DiccionarioPedro["notas"]) / len(DiccionarioPedro["notas"])
promedioJuan = sum(DiccionarioJuan["notas"]) / len(DiccionarioJuan["notas"])

# Imprimir los diccionarios y los promedios
print("Diccionario Pedro: ", DiccionarioPedro)
print("Promedio de notas de Pedro: ", promedioPedro)

print("Diccionario Juan: ", DiccionarioJuan)
print("Promedio de notas de Juan: ", promedioJuan)
"""






#OTRA FORMA DE RESOLVERLO

# Crear los diccionarios con las notas de cada estudiante
DiccionarioPedro = dict(nombre="Pedro", notas=[4, 7, 5, 6])
DiccionarioJuan = dict(nombre="Juan", notas=[10, 7, 5, 2])

# Función para calcular el promedio sin usar sum() ni len()
def calcular_promedio_manual(estudiante):
    total = 0
    contador = 0
    for nota in estudiante["notas"]:
        total += nota
        contador += 1
    promedio = total / contador
    return promedio

# Calcular y mostrar los promedios
promedioPedro = calcular_promedio_manual(DiccionarioPedro)
promedioJuan = calcular_promedio_manual(DiccionarioJuan)

print(f"Promedio de notas de Pedro: {promedioPedro:}")
print(f"Promedio de notas de Juan: {promedioJuan:.2f}")