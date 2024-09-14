numeros = [4,7,42,15]
numero = 12.345678

# Número mayor de una lista, arroja EXCEPTION si contiene alguna cadena
print()
print(f"El número mayor: {max(numeros)}")

# Número menor de una lista, arroja EXCEPTION si contiene alguna cadena
print()
print(f"El número menor: {min(numeros)}")

# Redondear a N decimales
print()
print(round(numero,3))
print(round(numero,5))

# Retorna FALSE si es 0, vacío o NONE
print()
print(bool())
print(bool("Cadena..."))
print(bool(1))
print(bool(None))

# Suma números, arroja EXCEPTION si contiene alguna cadena
print()
print(sum(numeros))