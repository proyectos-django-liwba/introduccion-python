
# arreglo de string
list = [ "Javascript", "Java", "Python", "C#", "C++" ]
print(list)

# manejo de indices
print(list[0]) # Javascript

# manejo de indices negativos
print(list[-1]) # C++

# manejo de rangos
print(list[0:3]) # [ "Javascript", "Java", "Python" ]

# sobreescribir valores
list[0] = "Javascript ES6"
print(list)

# agregar valores al final
list.append("PHP")
print(list)

# agregar valores al inicio
list.insert(0, "Ruby")

# agregar valores en una posicion especifica
list.insert(3, "Ruby")
print(list)

# eliminar valores
list.remove("Ruby")
print(list)

# eliminar valores por indice
list.pop(0)
print(list)

# eliminar el ultimo valor
list.pop()
print(list)

# arreglo de numeros
list = [ 1, 2, 3, 4, 5 ]
print(list)

# arreglo de booleanos
list = [ True, False, True, False ]

# arreglo de diferentes tipos de datos
list = [ "Javascript", 1, True, "C#", 2, False ]
print(list)

# arreglo de arreglos
list = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(list)

# arreglo de objetos
list = [ { "name": "Javascript" }, { "name": "Java" }, { "name": "Python" } ]
print(list)


