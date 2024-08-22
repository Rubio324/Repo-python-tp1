def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    
    # Crear la versión invertida usando slicing
    #cadena_reversa = cadena[::-1]
    cadena_reversa = ""
    for char in cadena:
        cadena_reversa = char + cadena_reversa  # Construir la cadena inversa
    
    # Comparar la cadena limpia con su reversa
    return cadena == cadena_reversa
    

# Ejemplos de uso
print(es_palindromo("neuquen"))  # True
print(es_palindromo("radar"))    # True
print(es_palindromo("hello"))    # False
print(es_palindromo("A man a plan a canal Panama"))  # True