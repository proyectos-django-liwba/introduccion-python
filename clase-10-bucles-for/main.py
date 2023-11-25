import random


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in array:
    print(num)

# auto llenado de un array
array = [i for i in range(10)]
print(array)

# llenado aleatorio de un array
arrayAleatorio = []

for i in range(10):
    num = random.randint(1, 100)
    print(num)
    arrayAleatorio.append(num)

print(arrayAleatorio)
    
# solicita la cantidad de numeros para llenar el array
try:
    cantidad = int(input("Ingrese la cantidad de numeros: "))
    array = []
    for i in range(cantidad):
        num = random.randint(1, 100)
        array.append(num)
        
    print(array)
    
except:
    print("Error al ingresar la cantidad de numeros")