# Creando una función que devuelva los números primos desde 0 hasta el número definido.

def numeros_primos(num):
    for i in range(2, num-1): # Si dividimos por 1 y por si mismo, todo número diría que es primo, entonces los sacamos de la evaluación.
        if num % i == 0: return False
    return True

def agregar_primos(num):
    primos = []
    for i in range(3, num + 1): # Comenzamos la lista desde el 3, porque el 1 y el 2 los considera primos y llegamos hasta num + 1 para incluir el número evaluado
        resultado = numeros_primos(i)
        if resultado == True: primos.append(i)
    return primos

print(agregar_primos(1365))