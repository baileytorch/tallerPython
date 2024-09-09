nombre = True
bienvenida = "Hola {nombre} ¿Cómo estás?" # Así NO funciona
bienvenida2 = f"Hola {nombre} ¿Cómo estás?" # Así funciona

# Borrado de datos, al imprimir las variables no hay error, porque se borró después de asignarla
del nombre

# Definir variable con camelCase
nombreCompleto = "Erick Bailey"

# Definir variable con snake_case, recomendación de Python
nombre_completo = "Erick Bailey"

# Concatenar con +
bienvenida3 = "Hola " + nombreCompleto + " ¿Cómo estás?"

# Concatenar con +
bienvenida4 = "Hola " + nombreCompleto + " ¿Cómo estás?"

# Concatenar con f
bienvenida5 = f"Hola {nombre_completo} ¿Cómo estás?"

# print(nombre)
print(bienvenida)
print(bienvenida2)
print(bienvenida3)
print(bienvenida4)
print(bienvenida5)

# Operadores de pertenencia (in / not in)
print("Erick" in bienvenida) # Retorna True
print("Erick" not in bienvenida) # Retorna False
