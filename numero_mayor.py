class ColaSimple:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * (self.max + 1)  # Arreglo para la cola
        self.front = 0  # Inicio de la cola
        self.back = 0  # Final de la cola

    def es_vacia(self):
        return self.front == self.back

    def es_llena(self):
        return (self.back + 1) % (self.max + 1) == self.front

    def size(self):
        return (self.back - self.front + self.max + 1) % (self.max + 1)

    def enqueue(self, elemento):
        if not self.es_llena():
            self.back = (self.back + 1) % (self.max + 1)
            self.cola[self.back] = elemento  # Almacenar el nuevo elemento
        else:
            print("Cola llena...")

    def dequeue(self):
        elemento = None
        if not self.es_vacia():
            self.front = (self.front + 1) % (self.max + 1)
            elemento = self.cola[self.front]
            # Si la cola está vacía después de la eliminación
            if self.front == self.back:
                self.front = 0
                self.back = 0
        else:
            print("Cola vacía...")
        return elemento

    def mostrar(self):
        if self.es_vacia():
            print("Cola vacía...")
        else:
            if self.front < self.back:
                print(self.cola[self.front + 1:self.back + 1])
            else:
                print(self.cola[self.front + 1:self.max + 1] + self.cola[0:self.back + 1])

    def obtener_mayor(self):
        if self.es_vacia():
            print("Cola vacía...")
            return None
        else:
            mayor = self.cola[(self.front + 1) % (self.max + 1)]
            i = (self.front + 2) % (self.max + 1)
            while i != (self.back + 1) % (self.max + 1):
                if self.cola[i] > mayor:
                    mayor = self.cola[i]
                i = (i + 1) % (self.max + 1)
            return mayor

    def obtener_pares(self):
        if self.es_vacia():
            print("Cola vacía...")
            return []
        else:
            pares = []
            i = (self.front + 1) % (self.max + 1)
            while i != (self.back + 1) % (self.max + 1):
                if self.cola[i] % 2 == 0:
                    pares.append(self.cola[i])
                i = (i + 1) % (self.max + 1)
            return pares

# Función principal para interactuar con el usuario
def main():
    max_size = int(input("Ingrese el tamaño máximo de la cola: "))
    cola = ColaSimple(max_size)
    
    while True:
        print("\nOpciones:")
        print("1. Enqueue (Agregar elemento)")
        print("2. Dequeue (Eliminar elemento)")
        print("3. Mostrar cola")
        print("4. Obtener mayor")
        print("5. Obtener pares")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            elemento = int(input("Ingrese el elemento a agregar: "))
            cola.enqueue(elemento)
        elif opcion == 2:
            elemento = cola.dequeue()
            if elemento is not None:
                print(f"Elemento eliminado: {elemento}")
        elif opcion == 3:
            cola.mostrar()
        elif opcion == 4:
            mayor = cola.obtener_mayor()
            if mayor is not None:
                print(f"El mayor elemento es: {mayor}")
        elif opcion == 5:
            pares = cola.obtener_pares()
            print(f"Elementos pares: {pares}")
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
