
class Coche:
  __marca = ""
  __modelo = ""
  __color = ""
  __encendido = False


  # Constructor
  def __init__(self, marca, modelo, color):
    self.__marca = marca
    self.__modelo = modelo
    self.__color = color
  
  # Métodos
  def encender(self):
    self.__encendido = True
  
  def apagar(self):
    self.__encendido = False
    
  def get_encendido(self):
    return self.__encendido
  
  def set_marca(self, marca):
    self.__marca = marca
  
  def get_marca(self):
    return self.__marca
  
  def set_modelo(self, modelo):
    self.__modelo = modelo
    
  def get_modelo(self):
    return self.__modelo
  
  def set_color(self, color):
    self.__color = color
    
  def get_color(self):
    return self.__color
  

class Traccion():
  # Atributos
  __traccion = ""
  
  # Constructor
  def __init__(self, traccion):
    self.__traccion = traccion
  
  # Métodos
  def set_traccion(self, traccion):
    self.__traccion = traccion
    
  def get_traccion(self):
    return self.__traccion


# Herencia
class CocheDeportivo(Coche, Traccion):
  # Atributos
  __cv = 0
  
  # Constructor
  def __init__(self, marca, modelo, color,traccion, cv):
    Coche.__init__(self,marca, modelo, color)
    Traccion.__init__(self,traccion)
    self.__cv = cv
    
  # Métodos
  def set_cv(self, cv):
    self.__cv = cv
    
  def get_cv(self):
    return self.__cv
  
  def to_string(self):
    return "Marca: " + self.get_marca() + "\nModelo: " + self.get_modelo() + "\nColor: " + self.get_color() + "\nCV: " + str(self.__cv) + "\nTracción: " + self.get_traccion()
  
  
# Instanciar objetos
coche1 = CocheDeportivo("Audi", "A3", "Rojo", "4x4", 200)

print(coche1.to_string())

  