
# Programa 1: Búsqueda en matriz bidimensional

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == valor:
                return True, i, j  # Retornamos encontrado y posición
    return False, None, None  # No encontrado

# Valor a buscar
valor_buscado = 5

# Llamamos a la función
encontrado, fila, columna = buscar_en_matriz(matriz, valor_buscado)

# Mostramos el resultado
if encontrado:
    print(f"El valor {valor_buscado} se encontró en la posición (fila {fila}, columna {columna}).")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
