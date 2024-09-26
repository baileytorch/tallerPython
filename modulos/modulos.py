import saludar as sal # Importamos un módulo completo
# from saludar import saludar, saludar_formal # Acá sólo importamos la función requerida
# from saludar import saludar as saludin, saludar_formal as saludo # Acá sólo importamos la función requerida, camabiando su nombre

print(sal.saludar("Aquiles Brinco"))
print(sal.saludar_formal("Aquiles Brinco"))
print(dir(sal)) # Esto nos devuelve pripiedades y métodos que contiene el módulo importado