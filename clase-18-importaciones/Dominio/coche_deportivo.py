# importar clase que se encuentra en el mismo directorio
from .coche import Coche
from .traccion import Traccion


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
  
  