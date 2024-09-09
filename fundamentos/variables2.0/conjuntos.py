# Crear un conjunto con SET().No se pueden incluir datos variables, como una LISTA o DICCIONARIO, 
# pero si podemos incluir una TUPLA dentro del conjunto.
conjunto = set({"Armando","Casas",2500000,("Aquiles","Brinco",2500000)}) # Agregando TUPLA al CONJUNTO
# conjunto = set({"Armando","Casas",2500000,{"Aquiles","Brinco",2500000}}) # No se puede agregar LISTA al CONJUNTO

print()
print(type(conjunto))
print(conjunto)