# Crear un conjunto con SET([]).
# No se pueden incluir datos variables, como una LISTA o DICCIONARIO, 
# pero si podemos incluir una TUPLA dentro del conjunto.
# de esta forma se pueden crear conjuntos vacíos.

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

# Teoría de Conjuntos
teoria_conjunto_1 = {1,3,5,7}
teoria_conjunto_2 = {3,5,7}

# Verificar si es SUBCONJUNTO
resultado1 = teoria_conjunto_1.issubset(teoria_conjunto_2)
resultado2 = teoria_conjunto_2.issubset(teoria_conjunto_1)
resultado3 = teoria_conjunto_2 <= teoria_conjunto_1 # Menor o igual es lo mismo que preguntar si es subconjunto

print()
print(resultado1)
print(resultado2)
print(resultado3)

# Verificar si es SUPERCONJUNTO
resultado4 = teoria_conjunto_1.issuperset(teoria_conjunto_2)
resultado5 = teoria_conjunto_2.issuperset(teoria_conjunto_1)
resultado6 = teoria_conjunto_2 > teoria_conjunto_1 # Mayor es lo mismo que preguntar si es superconjunto

print()
print(resultado4)
print(resultado5)
print(resultado6)

# Verificar si hay algún elemento en común
resultado7 = teoria_conjunto_1.isdisjoint(teoria_conjunto_2) # Se verifica si con completamente distintos.
# Habiendo sólo 1 elemento en común, deja de ser distinto

print()
print(resultado7)