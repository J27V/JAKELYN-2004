# Función de ordenación (utilizaremos Bubble Sort para este ejemplo)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambiar los elementos

# Matriz 3x3
matriz = [
    [9, 2, 5],
    [4, 8, 1],
    [7, 6, 3]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1, índice 0)
fila_a_ordenar = 1  # Cambiar el índice según la fila que quieras ordenar

# Ordenar la fila específica
bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
