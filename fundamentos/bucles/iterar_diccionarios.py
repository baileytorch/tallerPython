diccionario = {
    "nombre":"Armando",
    "apellido":"Casas",
    "edad":25
}

print()
for clave in diccionario:
    print(f"Clave: {clave}")

print()
for clave_valor in diccionario.items():
    print(f"Clave y Valor: {clave_valor}")
    
print()
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]
    print(f"Clave: {clave},  Valor: {valor}")