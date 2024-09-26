# Al faltar el profesor a clases, los alumnos se organizan para hacerla ellos mismos.
# Un alumno será el profesor (el de mayor edad) y otro será su asistente (el de menor edad),
# pero no esta claro quienes serán.

# Primero se debe ingresar el nombre y la edad de los asistentes a clases.
def  listado_estudiantes(cantidad_estudiantes):
    estudiantes = []
    for i in range(cantidad_estudiantes):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        estudiante = (nombre, edad)
        estudiantes.append(estudiante)
    estudiantes.sort(key= lambda x: x[1]) # Se ordena de forma decreciente por el segundo parámetro, que es la edad
    
    asistente = estudiantes[0][0] # El primer valor es la posición del elemento, el primer elemento = 0, el segundo valor es el parámetro nombre
    profesor = estudiantes[-1][0] # Listado -1 devuelve el último valor del listado.
    return asistente, profesor

asistente, profesor = listado_estudiantes(3)

print(f"El profesor es {profesor} y su asistete es {asistente}")