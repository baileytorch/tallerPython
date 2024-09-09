diccionario = {
    "Nombre" : "Erick",
    "Apellido" : "Bailey",
    "Edad" : 49,
    "Profesión" : "Desarrollador"
}

claves = diccionario.keys() # Obtenemos las claves, sirven para iteraciones
print(claves)
print(diccionario.get("Edad")) # Obtener un elemento

diccionario.pop("Apellido") # Elimina un item específico
print(diccionario)
print(diccionario.items()) # Diccionario iterable

diccionario.clear() # Elimina todos los elementos del diccionario