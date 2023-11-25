
# Generar tablas de multiplicar del 1 al 10

try:
    numero = int(input("Ingrese un número: "))
    if numero > 0 and numero <= 10:
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
            
    else:
        print("El número debe estar entre 1 y 10")
        
except ValueError:
    print("Debe ingresar un número entero") 
    