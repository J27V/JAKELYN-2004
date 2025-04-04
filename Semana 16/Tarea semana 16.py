# Abrir archivo para escritura
Archivo = open('my_notes.txt', "w")

# Escribir 3 líneas
Archivo.write('En unos días empezaré las evaluaciones del parcial.\n')
Archivo.write('Que estoy feliz de que estamos a un paso de culminar el primer semestre.\n')
Archivo.write('Al iniciar este proceso tenía miedo de no poder lograrlo, pero con dedicación todo es posible.\n')

# Cerrar el archivo después de escribir
Archivo.close()

# Abrir archivo para lectura
Archivo = open('my_notes.txt', 'r')

# Leer línea por línea e imprimir
print(Archivo.readline().strip())  # Lee la primera línea y la imprime
print(Archivo.readline().strip())  # Lee la segunda línea y la imprime
print(Archivo.readline().strip())  # Lee la tercera línea y la imprime

# Cerrar el archivo después de leer
Archivo.close()


