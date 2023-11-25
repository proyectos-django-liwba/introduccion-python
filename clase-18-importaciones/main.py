# importar clase que se encuentra en otro directorio
from Dominio.coche_deportivo import CocheDeportivo

# Instanciar objetos
coche1 = CocheDeportivo("Audi", "A3", "Rojo", "4x4", 200)

print(coche1.to_string())

  