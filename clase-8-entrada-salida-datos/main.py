
name = input("What is your name? ")
print("Hello, " + name + "!")

age = input("How old are you? ")
print(f"You are {age} years old.")


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2 # no es una suma, es una concatenacion
print(result)

# validar si es un numero
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

# validar que solo ingrese numeros
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
try:
    result = int(num1) + int(num2)
    print(result)
except:
    print("Invalid input")

# uso de ciclo while para validar que solo ingrese numeros
while True:
    try:
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
        result = int(num1) + int(num2)
        print(result)
        break
    except:
        print("Invalid input")
        
# indicar en el input que solo se aceptan numeros
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2  # ahora si es una suma
print(result)

# indicar en el input booleanos
booleano = bool(input("Enter a number: "))
print(booleano)

# indicar en el input string
string = str(input("Enter a number: "))
print(string)

# indicar en el input float
flotante = float(input("Enter a number: "))
print(flotante)
