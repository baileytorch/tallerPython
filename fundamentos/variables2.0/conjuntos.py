# Crear un conjunto con SET([]).
# No se pueden incluir datos variables, como una LISTA o DICCIONARIO, 
# pero si podemos incluir una TUPLA dentro del conjunto.

conjunto = set(["Armando","Casas",2500000,("Aquiles","Brinco",2500000)]) # Agregando TUPLA al CONJUNTO
# conjunto = set(["Armando","Casas",2500000,["Aquiles","Brinco",2500000]]) # No se puede agregar LISTA al CONJUNTO
# conjunto = set(["Armando","Casas",2500000,{"Aquiles","Brinco",2500000}]) # No se puede agregar DICCIONARIO al CONJUNTO
# conjunto2 = {conjunto,"Nuevo Dato"} # No se puede poner un conjunto dentro de otro
conjunto2 = frozenset(["Dato1","Dato2"]) # Transformamos el conjunto en un elemento "hashable"
conjunto3 = set([conjunto2,"dato3"]) # Podemos incluir un elemento FROZENSET dentro del conjunto

# Trabajando el mismo concepto de conjunto sin SET([])
conjunto_frozenset = frozenset(["Dato1","Dato2"])
conjunto_sin_set_2 = {conjunto_frozenset,"dato3"}

print()
print(type(conjunto))
print(conjunto)

print()
print(type(conjunto3))
print(conjunto3)

print()
print(type(conjunto_sin_set_2))
print(conjunto_sin_set_2)