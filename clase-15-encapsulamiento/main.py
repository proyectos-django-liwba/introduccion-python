# encapsulamiento consiste en ocultar los atributos de una clase para que 
# no puedan ser accedidos desde fuera de la clase
# para ello se utilizan los métodos getters y setters que son los que permiten
# acceder a los atributos de una clase desde fuera de la misma

# declarar propiedades privadas
# para ello se antepone dos guiones bajos al nombre del atributo

class Coche:
  marca = ""
  modelo = ""
  color = ""
  __encendido = False


  # Constructor
  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color
  
  # Métodos
  def encender(self):
    self.__encendido = True
  
  def apagar(self):
    self.__encendido = False
    
  def get_encendido(self):
    return self.__encendido


# crear instancia de la clase
coche1 = Coche("Mazda", "MX5", "Rojo")
# acceder a metodos
coche1.encender()
# sin encapsulamiento se puede acceder a los atributos directamente
# evitando el uso de los metodos definidos
#coche1.encendido = False # esto ahora genera un error
coche1.__encendido = False # esto ahora genera un error o no se ejecuta
print(coche1.get_encendido())
# con encapsulamiento no se puede acceder a los atributos directamente
#print(coche1.encendido) # esto ahora genera un error
coche1.apagar()
print(coche1.get_encendido())

