
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


# Herencia

class CocheDeportivo(Coche):
  # Atributos
  __cv = 0
  
  # Constructor
  def __init__(self, marca, modelo, color, cv):
    super().__init__(marca, modelo, color)
    self.__cv = cv
    
  # Métodos
  def set_cv(self, cv):
    self.__cv = cv
    
  def get_cv(self):
    return self.__cv
  
  def to_string(self):
    return "Marca: " + self.get_marca() + "\nModelo: " + self.get_modelo() + "\nColor: " + self.get_color() + "\nCV: " + str(self.__cv)
  
  
# Instanciar objetos

coche1 = CocheDeportivo("Audi", "A3", "Rojo", 200)

print(coche1.to_string())

  