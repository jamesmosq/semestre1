# Ejercicio 4: Descuento en una Tienda

precio_I = float(input("Ingresa el precio original del artículo: "))
porcentaje_D = float(input("Ingresa el porcentaje de descuento: "))

descuento = precio_I * (porcentaje_D / 100)
precio_final = precio_I - descuento

print(f"El precio final con {porcentaje_D}% de descuento es: {precio_final}")
