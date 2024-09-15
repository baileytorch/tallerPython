def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, ¿cómo estás {adjetivo}?"

print()
print(frase("grandioso", "Brinco", "Aquiles")) # Si no se entregan los parámetros en orden, el resultado NO es el esperado
print(frase(adjetivo="grandioso", apellido="Brinco", nombre="Aquiles")) # Forzando parametros, KEYWORD ARGUMENTS

def frase2(nombre,apellido,adjetivo="Campeón"): # Este parámetro queda como opcional y definido
    return f"Hola {nombre} {apellido}, ¿cómo estás {adjetivo}?"
print()
print(frase2("Aquiles","Brinco")) # No es necesario pasar el parámetro que ya está definido
print(frase2("Aquiles","Brinco", adjetivo="máquina")) # Podemos cambiar parámetros forzados
