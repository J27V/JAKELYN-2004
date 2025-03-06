# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Función para buscar el valor
def buscar_valor(matriz, valor):
    for i in range(3):  # Recorremos las filas (sabemos que la matriz es 3x3)
        for j in range(3):  # Recorremos las columnas
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (i, j)
    return None  # Si no lo encuentra

# Llamamos a la función
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if resultado:
    print(f"Valor {valor_a_buscar} encontrado en la posición {resultado}")
else:
    print(f"Valor {valor_a_buscar} no encontrado.")

