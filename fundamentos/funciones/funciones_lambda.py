numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Creaundo una función normal para retornar pares
def es_par(num):
    if(num%2 == 0):
        return True

# Creaundo una función normal para retornar pares
def es_impar(num):
    if(num%2 != 0):
        return True

# Usamos la función FILTER cuyo primer parámetro es una función
print()
print(list(filter(es_par,numeros)))
print(list(filter(es_impar,numeros)))

# Lambda crea funciones anónimas que luego pueden ser almacenadas en una variable