
# validar un numero si es par o impar

try:
    numero = int(input("Ingrese un numero: "))
    
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
except:
    print("Error al ingresar el numero")
    
# validar un numero si es positivo o negativo

try:
    positivo = int(input("Ingrese un numero: "))
    
    if positivo > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
except:
    print("Error al ingresar el numero")
    
# validar si es mayor de edad o menor de edad

try: 
    edad = int(input("Ingrese su edad: "))
    
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
except:
    print("Error al ingresar la edad")
    
    
# validar si que no sea menor de edad
try:
    edad = int(input("Ingrese su edad: "))
    
    if not edad == 18:
        print("Bienvenido")
    else:
        print("No es mayor de edad")
        
except:
    print("Error al ingresar la edad")
    

# condicional anidado
try:
    numero = int(input("Ingrese un numero: "))
    
    if numero > 0:
        print("El numero es positivo")
    elif numero == 0:
        print("El numero es cero")
    else:
        print("El numero es negativo")
except:
    print("Error al ingresar el numero")
    
# condicional anidado internamente

try:
    numero = int(input("Ingrese un numero: "))
    
    if numero >= 0:
        if numero == 0:
            print("El numero es cero")
        else:
            print("El numero es positivo")
    else:
        print("El numero es negativo")
except:
    print("Error al ingresar el numero")

# NOTA: mas de dos condiciones anidadas internamente, se debe extraer el codigo a una funcion