# Crear diccionarios con dict()
# de esta forma se pueden crear diccionarios vacíos.
diccionario = dict(nombre="Armando",apellido="Casas")
diccionario = frozenset({"nombre","apellido","Brinco"}) # Transformamos el conjunto en un elemento "hashable"

print()
print(type(diccionario))
print(diccionario)