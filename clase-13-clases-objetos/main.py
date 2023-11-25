
class Vehiculo:
  #pass # permite crear una clase vacía
  marca = ""
  color = ""
  modelo = ""
  anio = 0
  # definir constructor
  def __init__(self, marca, color, modelo, anio):
    self.marca = marca
    self.color = color
    self.modelo = modelo
    self.anio = anio


# Instanciar una clase sin constructor
#vehiculo1 = Vehiculo()

# Instanciar una clase con constructor
vehiculo1 = Vehiculo("Mazda", "Rojo", "CX-5", 2019)

# Asignar valores a las propiedades
vehiculo1.marca = "Toyota"

vehiculo2 = Vehiculo("Toyota", "Blanco", "Corolla", 2018)

#print(vehiculo1) # indica la ubicación en memoria
print(vehiculo1.marca)

print(vehiculo2.marca)

# imprimir un objeto
print(vars(vehiculo1))