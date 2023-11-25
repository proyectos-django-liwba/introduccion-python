
# Ciclo while
contador = 1

while contador <= 10: 
    print(contador)
    contador += 1
    
print("Fin del ciclo while")

# ciclo do while

contador = 1

while True: # en python no existe el ciclo do while, pero se puede simular
    print(contador)
    contador += 1
    if contador > 10:
        break
      
print("Fin del ciclo do while")


# switch case, no existe en python, pero se puede simular

def switch_demo(argument):
    switcher = { # diccionario
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    # get(argument, "Mes invalido") es un metodo del diccionario que devuelve el valor de la clave argument,
    # si no existe devuelve el segundo parametro
    return switcher.get(argument, "Mes invalido") # el segundo parametro es el valor por defecto
  
print(switch_demo(1))
print(switch_demo(13))

print(switch_demo(2))

