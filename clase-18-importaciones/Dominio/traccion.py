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