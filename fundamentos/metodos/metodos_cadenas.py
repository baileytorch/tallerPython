string1 = "Erick Bailey"
string2 = "Desarrollador de Sistemas"

print(dir(string1)) # La función DIR entrega todos los métodos que se pueden usar con el tipo de datos que posee

print("Todo en MAYÚSCULAS: " + string1.upper())
print("Todo en MINÚSCULAS: " + string1.lower())
print("Primera letra MMAYÚSCULA: " + string1.capitalize())

print(f"Buscamos Bai: {string1.find("Bai")}") # Si FIND no encuentra el texto, devuelve -1
#print(f"Buscamos Bai: {string1.index("9")}") # Si INDEX no encuentra el texto, devuelve un error
print(f"Contamos a: {string1.count("a")}") # cuenta la cantidad de ocurrencias del texto
print(f"Contamos x: {string1.count("x")}")

print(f"Empieza con Eri? {string1.startswith("Eri")}")
print(f"Termina con Eri? {string1.endswith("Eri")}")

print(f"Contamos caracteres: {len(string1)}")
print(f"Reemplazamos Erick: {string1.replace("Erick", "ERICK")}")

cadena_separada = string1.split(" ")
print(cadena_separada)
print(cadena_separada[1])

