"""
Programa que calcula el total a
   pagar en una tienda después de aplicar un descuento.
"""
def calcular_descuento(precio, descuento):
    # Calcula el precio final aplicando el descuento.
    precio_final = precio - (precio * descuento / 100)
    return precio_final

# Ejemplo 1
precio_original_1 = 500  # Precio original del primer producto
descuento_1 = 20  # Porcentaje de descuento

precio_con_descuento_1 = calcular_descuento(precio_original_1, descuento_1)
print(f"Ejemplo 1: El precio original es: ${precio_original_1}, con un descuento del {descuento_1}%. El precio final es: ${precio_con_descuento_1:.2f}")

# Ejemplo 2
precio_original_2 = 1200  # Precio original del segundo producto
descuento_2 = 15  # Porcentaje de descuento

precio_con_descuento_2 = calcular_descuento(precio_original_2, descuento_2)
print(f"Ejemplo 2: El precio original es: ${precio_original_2}, con un descuento del {descuento_2}%. El precio final es: ${precio_con_descuento_2:.2f}")

# Ejemplo 3
precio_original_3 = 50  # Precio original del tercer producto
descuento_3 = 10  # Porcentaje de descuento

precio_con_descuento_3 = calcular_descuento(precio_original_3, descuento_3)
print(f"Ejemplo 3: El precio original es: ${precio_original_3}, con un descuento del {descuento_3}%. El precio final es: ${precio_con_descuento_3:.2f}")
