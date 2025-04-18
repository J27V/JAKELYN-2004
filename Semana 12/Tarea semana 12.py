# Crear una matriz 3D para almacenar las temperaturas
# La estructura es: [cuidad][día de la semana][semana]
temperaturas = [
    [  # Cuidad:  Quito
        [22, 23, 24],  # Semana 1: Lunes, Martes, Miércoles
        [21, 22, 23],  # Semana 2: Lunes, Martes, Miércoles
        [20, 21, 22],  # Semana 3: Lunes, Martes, Miércoles
    ],
    [  # Cuidad:  Manabi
        [18, 19, 20],  # Semana 1: Lunes, Martes, Miércoles
        [17, 18, 19],  # Semana 2: Lunes, Martes, Miércoles
        [21, 22, 23],  # Semana 3: Lunes, Martes, Miércoles
    ],
    [  # Cuidad:  Cuenca
        [28, 29, 30],  # Semana 1: Lunes, Martes, Miércoles
        [27, 28, 29],  # Semana 2: Lunes, Martes, Miércoles
        [30, 31, 32],  # Semana 3: Lunes, Martes, Miércoles
    ]
]

# nombres de las cuidades
cuidades = ["Quito", "Manabi", "Cuenca"]

for cuidad in range(len(temperaturas)):  # Iterar sobre las cuidades
    print(f"Pomedios para la cuidad de {cuidades[cuidad]}:")
    for semana in range(len(temperaturas[cuidad])):  # Iterar sobre las semanas
        suma_temperaturas = sum(temperaturas[cuidad][semana])  # Sumar las temperaturas de los 3 dias
        promedio = suma_temperaturas / len(temperaturas[cuidad][semana])  # Calcular el promedi o
        print(f" semana {semana + 1}: promedio temperatura  =  {promedio:.2f}ºC")
    print("")  # linea en blanco para separar las cuidades
