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
    chars = "abcdefghi"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    print(contraseña)

print()
crear_contraseña_random(1)
crear_contraseña_random(5)
crear_contraseña_random(10)