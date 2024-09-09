# Las LISTAS son colecciones ordenadas y mutables,
# es decir, son modificables una vez creadas.
# Pueden almacenar elementos de diferentes tipos al mismo tiempo,
# ideales para almacenar una colección de datos que necesita ser modificada o accedida por índices.
# Almacena los datos en 2 espacios de memoria, el índice y el dato mismo.

print("\nTrabajando con LISTAS.\n======================")
lista = ["Armando Casas", True, 1.73]
print(lista)

lista[1] = "Nuevo Valor" # Cambio válido, acceso al elemento por ÍNDICE
print(lista[1])
print(f"{lista}\n")

# Los DICCIONARIOS son colecciones no ordenadas de pares KEY : VALUE, usando 2 espacios de memoria.
# Permiten almacenar datos de manera que cada elemento pueda ser recuperado, actualizado o eliminado usando su clave.

print("Trabajando con DICCIONARIOS.\n============================")
diccionario = {
    'nombre' : 'Armando Casas',
    'Está emocionado?' : True,
    'Altura' : 1.73
}
print(diccionario)

diccionario['nombre'] = "Nuevo Valor" # Cambio válido, acceso al elemento por KEY
print(diccionario['nombre'])
print(f"{diccionario}\n")

# Los CONJUNTOS o sets son colecciones desordenadas, NO indexadas de elementos únicos, NO almacena datos duplicados.
# Son ideales para realizar operaciones de conjunto como uniones, intersecciones y diferencias,
# así como para eliminar elementos duplicados de una colección.
# NO se puede acceder a los elementos por un ÍNDICE ni por una CLAVE.

print("Trabajando con CONJUNTOS.\n==========================")
conjunto = {"Armando Casas", True, 1.73}
# conjunto[1] = "Nuevo Valor" # Cambio NO válido, no se puede acceder a los elementos por ÍNDICE
# print(sorted(conjunto)) # Si se tiene distintos tipos de datos, no se puede aplicar la función SORTED para ordenar
print(conjunto)

conjunto.add("Nuevo Valor") # Se agrega un nuevo valor al conjunto.
conjunto.add("Nuevo Valor") # El conjunto ya tiene este valor, NO se agrega nuevamente.
print(f"{conjunto}\n")

# Las TUPLAS son colecciones ordenadas e inmutables.
# Se utilizan para almacenar una secuencia de valores que no deben cambiar a lo largo del programa.
# Son más rápidas que las listas, por NO usar un par de valores para cada dato
# y protegen los datos de modificaciones accidentales.
# Su uso más general es para manejar datos de sólo lectura.

print("Trabajando con TUPLAS.\n======================")
tupla = ("Armando Casas", True, 1.73)
print(tupla)
print(f"{tupla[0]}\n")

# tupla[1] = "Nuevo Valor" # Cambio NO válido
# print(tupla)