frutas = ["naranja","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Aquiles Brinco"
numeros = [1,2,3,4,5]

print()
for fruta in frutas:
    print(f"La fruta escogida es: {fruta}")

# Recorrer la lista, dejando de lado objetos con CONTINUE,
# evitando cualquier instrucción posterior dentro del ciclo.
print()
for fruta in frutas:
    if fruta == "naranja":
        continue # Esta instrucción envía la ejecución del código a la siguiente iteración
    print(f"La fruta escogida es: {fruta}")

# Terminando ciclo con BREAK, si ponemos un else después del ciclo, tampoco se ejecuta
print()
for fruta in frutas:
    if fruta == "pera":
        break # Esta instrucción termina la ejecución del ciclo
    print(f"La fruta escogida es: {fruta}")
print("Ciclo terminado...")

# Las cadenas se recorren caracter por caracter
print()
for letra in cadena:
    print(letra)

# Manualmente podemos usar los ciclos para ejecutar acciones
print()
numeros_duplicados = list() # Creamos una lista vacía
for numero in numeros:
    numeros_duplicados.append(numero * 2)
print(numeros_duplicados)

# Ejecutando el ciclo en una línea
numeros_duplicados = [num ** 2 for num in numeros]
print(numeros_duplicados)