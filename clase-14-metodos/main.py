class Coche:
  marca = ""
  modelo = ""
  color = ""
  encendido = False
  velocidad = 0

  # Constructor
  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color
  
  # Métodos
  def encender(self):
    self.encendido = True
    
  def apagar(self):
    self.encendido = False
    
  def acelerar(self):
    self.velocidad += 1
    
  def frenar(self):
    self.velocidad -= 1
    


# crear una instancia de la clase Coche
coche1 = Coche("Ford", "Fiesta", "Rojo")

print(coche1.encendido)

# Llamar al método encender
coche1.encender()

print(coche1.encendido)

if coche1.encendido:
  print("El coche está encendido")
else:
  print("El coche está apagado")
  
# Llamar al método acelerar

if coche1.encendido:
  
  # si esta encendido, acelerar
  for i in range(1, 41):
    coche1.acelerar()
    print("La velocidad actual es de: " + str(coche1.velocidad))
    
  # si la velocidad es mayor o igual a 40, frenar
  if coche1.velocidad >= 40:
    for i in range(1, 41):
      coche1.frenar()
      print("La velocidad actual es de: " + str(coche1.velocidad))
      
  # si la velocidad es menor o igual a 0, apagar
  if coche1.velocidad <= 0:
    coche1.apagar()
    print("El coche está apagado")
  else:
    print("El coche está encendido")

else:
  print("El coche está apagado")
  coche1.encender()