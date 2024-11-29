# NanoEspinoza *E00000404309*
# NanoxNet_Corp

import os
import time

class FIFO:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        if self.elementos:
            return self.elementos.pop(0)
        else:
            return None

directorio_temporal = "NanoxNet_corp"
os.makedirs(directorio_temporal, exist_ok=True)  

cola = FIFO()

# Crear y agregar archivos
for i in range(1, 7):
    archivo = os.path.join(directorio_temporal, f"Nanito_{i}.txt")
    with open(archivo, "w") as f:
        f.write(f"Contenido de {archivo}")
    cola.agregar(archivo)

print("Elementos en la cola:")
for elemento in cola.elementos:
    print(elemento)

# Eliminar archivos 
while cola.elementos:
    elemento = cola.eliminar()
    time.sleep(5)
    if os.path.exists(elemento):
        os.remove(elemento)
        print(f"Elemento {elemento} eliminado")
    else:
        print(f"Elemento {elemento} no encontrado")

# eliminador de carpeta
if not os.listdir(directorio_temporal):  
    os.rmdir(directorio_temporal)  
    print(f"Directorio temporal {directorio_temporal} eliminado")
