# Creando TUPLAS con TUPLE(), en este caso se le pasa una lista y crea una tupla
# de esta forma se pueden crear tuplas vacías.
tupla_con_tuple = tuple(["Aquiles","Brinco",2500000])

# La TUPLA se puede crear con paréntesis o sin ellos,
# con valores separados por comas
tupla_sin_parentesis = "Aquiles","Brinco",2500000
tupla_sin_parentesis_1_dato = "Armando",

print()
print(type(tupla_con_tuple))
print(f"{tupla_con_tuple}\n")

print(type(tupla_sin_parentesis))
print(f"{tupla_sin_parentesis}\n")

print(type(tupla_sin_parentesis_1_dato))
print(f"{tupla_sin_parentesis_1_dato}\n")