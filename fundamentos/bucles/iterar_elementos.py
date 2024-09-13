# Estas iteraciones funcionan para listas, tuplas y conjuntos
animales = ["gato","perro","loro","cocodrilo"]
numeros = [20,30,40,50]

print()
for animal in animales:
    print(f"El animal en esta iteración es '{animal}'")

print()   
for numero in numeros:
    resultado = numero * numero
    print(f"{numero} * {numero} = {resultado}")
    
# Para iterar 2 listas, deben tener la misma cantidad de elementos
contador = 0
print() 
for animal,numero in zip(animales,numeros):
    contador = contador + 1
    print(f"Lista animales, elemento {contador} = {animal}")
    print(f"Lista numeros, elemento {contador} = {numero}")

# Forma incorrecta pero funcional de iterar, NO funciona en conjuntos
print()
for num in range(5,10): # Primer parámetro es donde inicia y segundo parámetro donde termina, sin incluirlo
    print(num)

print()
for num in range(10): # Cuando recibe sólo 1 parámetro, inicia en 0 y termina en el número indicado, sin incluirlo
    print(num)

print()
for num in range(len(numeros)): # Se itera de acuerdo a la cantidad de elementos
    print(num)


# Forma correcta de iterar por índices
print()
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice} y el valor es: {valor}")

# Con else... Es usado para ejecutar siempre algo al terminar el bucle
print()
for numero in numeros:
    print(f"Ejecutando el bucle, elemento actual: {numero}")
else:
    print("El bulce ha terminado")