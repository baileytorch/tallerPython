# DESEMPAQUETADO en variables, pasamos los datos de datos compuestos a variable
# se debe crear la misma cantidad de variables que de datos

datos_tupla = ("Armando","Casas",2500000)
datos_lista = ["Aquiles","Brinco",2500000]

nombre_tupla,apellido_tupla,sueldo_tupla = datos_tupla
nombre_lista,apellido_lista,sueldo_lista = datos_lista

print("\nDatos de Tupla\n==============")
print(f"Nombre: {nombre_tupla}")
print(f"Apellido: {apellido_tupla}")
print(f"Sueldo: {sueldo_tupla}")

print("\nDatos de Lista \n==============")
print(f"Nombre: {nombre_lista}")
print(f"Apellido: {apellido_lista}")
print(f"Sueldo: {sueldo_lista}")