lista = list(["Erick Bailey", 48])
print(lista)
print(f"Cantidad de elementos: {len(lista)}")

lista.append("Desarrolador")
print(lista)

lista.insert(1,True) # Agrega un elemento en un índice indicado
print(lista)

lista.extend([1,False]) # Agrega una lista con varios elementos
print(lista)

lista.pop(1) # Elimina un elemento en un índice indicado
lista.pop(-1) # Elimina el último elemento
lista.remove(1) # Elimina un elemento por su valor
print(lista)

lista.clear() # Elimina todos los elementos de la lista

lista2 = list([1,2,3,6,9,4])
lista2.sort() # Ordena los elementos de la lista, con parámetros se puede cambiar el orden
print(lista2)
lista2.reverse() # Invierte el orden de la lista
print(lista2)