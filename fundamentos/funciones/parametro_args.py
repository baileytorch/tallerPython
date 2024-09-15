# Sumamos números, de forma NO óptima
def suma(a,b):
    return a + b

# Sumar una lista nos permite pasarle muchos valores y obtener un resultado
# pero tampoco es la forma óptima de hacerlo, los argumentos de la función deberían ser indefinidos
def suma_lista(numeros):
    numeros_sumados = 0
    for numero in numeros:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

# Usamos el parámetro ARGS
def suma_args(*numeros): # Con * transformamos todos los parámetros en 1 solo
    return sum(numeros)

def suma_nombre_args(nombre,*numeros): # Cualquier parámetro anterior al * se puede ingresar, * marca el último parámetro
    return f"Hola {nombre}, la suma de tus números es: {sum(numeros)}"

# Esta sería la forma más óptima, porque podemos usar cualquier cantidad de parámetros e internamente se controlan
def suma_args_interno(numeros): # Ahora usamos el ARGS dentro de la función, pasando muchos parámetros
    return sum([*numeros]) # Acá transformamos el parámetro en una lista que recibe multiples parámetros

print()
print(suma(3,7))
# print(suma(3,5,7)) # Esto arroja un error al pasarle 3 argumentos
# print(suma([3,4,5])) # Si lo pasamos como una lista, arroja un error porque falta el segundo argumento
print(suma_lista([3,4,5])) # Si lo pasamos como una lista, suma todo sin problemas
print(suma_args(1,2,3,4,5,6,7,8,9)) # Pasamos muchos argumentos, suma todo sin problemas
print(suma_nombre_args("Aquiles Brinco",1,2,3,4,5,6,7,8,9)) # Usando más parámetros, suma todo sin problemas
print(suma_args_interno([1,2,3,4,5,6,7,8,9])) # Le pasamos una lsita como parámetro

