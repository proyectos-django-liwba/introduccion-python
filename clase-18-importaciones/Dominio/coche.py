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