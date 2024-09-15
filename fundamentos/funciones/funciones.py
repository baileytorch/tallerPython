def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "hermosa"
    elif (sexo == "hombre"):
        adjetivo = "campeón"
    else:
        adjetivo = "XD"
    print(f"Hola {nombre}, ¿Cómo estás {adjetivo}?")

print()
saludar("Aquiles Brinco","HOMBRE")
saludar("Zoila Cuevas","mujER")
saludar("Débora Melo","no binario")

# Crear una función que crea una contraseña al azar
def crear_contraseña_random(num):
    chars = "abcdefghi" # Creamos caracteres aleatorios
    num_entero = str(num) # Convertimos a STRING el número ingresado
    num = int(num_entero[0]) # Obtenemos sólo el primer caracter (número) ingresado y lo convertimos a numero
    c1 = num - 2 # Usamos ese número para transformarlo en otro número NUMERO - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return (contraseña, num) # De esta forma retornamos una tupla con el valor de una función para luego usarlo

print()
respuesta, numwero_usado = crear_contraseña_random(1) # Obtenemos los valores desempaquetando
print(f"Tu nueva contraseña: {respuesta}, con el número: {numwero_usado}")

respuesta, numwero_usado = crear_contraseña_random(5) # Obtenemos los valores desempaquetando
print(f"Tu nueva contraseña: {respuesta}, con el número: {numwero_usado}")

respuesta = crear_contraseña_random(10) # Obtenemos los valores por índice
print(f"Tu nueva contraseña: {respuesta[0]}, con el número: {respuesta[1]}")