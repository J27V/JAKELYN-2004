# Crear un diccionario con información ficticia sobre una persona
informacion_personal = {
    "nombre": "Juliana veloz",
    "edad": 21,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
print("Ciudad original:", informacion_personal["ciudad"])  # Muestra la ciudad original
informacion_personal["ciudad"] = "Guayaquil"  # Modificamos la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])  # Muestra la nueva ciudad

# Agregar una nueva clave-valor para representar el teléfono de la persona
informacion_personal["telefono"] = "0963814927"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0963814927"  # Si no existe, se agrega un número ficticio

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las modificaciones
print("Diccionario final:", informacion_personal)
