# Creando una función que devuelva los números de la serie Fibonacci hasta el número definido.

def fibonacci(num):
    a,b = 0, 1
    lista_fibonacci = [0] # Incluimos manualmente el 0 en la lista
    for i in range(num):
        if b > num: return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a, b = b, a + b

print(fibonacci(55))