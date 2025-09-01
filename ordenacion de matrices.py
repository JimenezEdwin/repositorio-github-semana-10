# Programa 2: Ordenación de una fila en matriz bidimensional

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [9, 8, 7],
    [3, 1, 2],
    [6, 5, 4]
]

# Función de Bubble Sort para ordenar una lista (fila) en orden ascendente
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, indice_fila):
    if 0 <= indice_fila < len(matriz):
        bubble_sort(matriz[indice_fila])  # Ordenamos la fila in-place

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegimos ordenar la fila 1 (segunda fila, índice 1)
ordenar_fila(matriz, 1)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)