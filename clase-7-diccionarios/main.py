
# Diccionarios, son estructuras de datos que nos permiten almacenar valores de diferente tipo
# como enteros, cadenas de texto, listas e incluso otras funciones.
# La principal caracteristica de los diccionarios es que los datos se almacenan asociados a una
# clave de tal forma que se crea una asociacion de tipo clave:valor para cada elemento almacenado.
# Los elementos almacenados no estan ordenados. El orden es indiferente a la hora de almacenar

data = {"name": "Juan", "lastname": "Perez", "age": 28, "city": "Bogota"}
print(data)

# Acceder a un elemento del diccionario
print(data["name"])

# Modificar un elemento del diccionario
data["age"] = 30
print(data)

# Eliminar un elemento del diccionario
del data["city"]
print(data)

# Recorrer un diccionario
for key, value in data.items():
    print(key, ":", value)
    
# Recorrer las claves de un diccionario
for key in data.keys():
    print(key)
    
# Recorrer los valores de un diccionario
for value in data.values():
    print(value)
    
# Comprobar si existe una clave en el diccionario
print("name" in data)
print("city" in data)

# Comprobar si existe un valor en el diccionario
print("Juan" in data.values())
print("Bogota" in data.values())

# Longitud de un diccionario
print(len(data))

# Limpiar un diccionario
data.clear()
print(data)

# Eliminar un diccionario
del data
print(data) # NameError: name 'data' is not defined