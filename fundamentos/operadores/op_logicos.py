# AND
resultado1 = True & True # Devuelve TRUE
resultado2 = False & True # Devuelve FALSE
resultado3 = True & False # Devuelve FALSE
resultado4 = False & False # Devuelve FALSE

# OR
resultado5 = True | True # Devuelve TRUE
resultado6 = False | True # Devuelve TRUE
resultado7 = True | False # Devuelve TRUE
resultado8 = False | False # Devuelve FALSE

# NOT
resultado9 = not True # Devuelve FALSE
resultado10 = not False # Devuelve TRUE

print(f"True & True = {resultado1}")
print(f"False & True = {resultado2}")
print(f"True & False = {resultado3}")
print(f"False & False = {resultado4}")

print(f"True | True = {resultado5}")
print(f"False | True = {resultado6}")
print(f"True | False = {resultado7}")
print(f"False | False = {resultado8}")

print(f"not True = {resultado9}")
print(f"not False = {resultado10}")