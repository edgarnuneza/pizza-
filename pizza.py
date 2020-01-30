from ingrediente import Ingrediente

class Pizza:

    def __init__(self, tamaño, ingredientes, precio):
        self.tamaño = tamaño
        self.ingredientes = list(ingredientes)
        self.precio = precio

    def __init__(self, tamaño, precio):
        self.tamaño = tamaño
        self.precio = precio
        self.ingredientes = list()

    def preparar(self):
        print('Se esta preparando la pizza')

    def empaquetar(self):
        print('Empaquetando pizza')

    def mostrarPizza(self):
        print('Tamaño', self.tamaño)
        print('Lista de ingredientes')

        for ingrediente in self.ingredientes:
            print(ingrediente)

        print('Precio:', self.precio)

    def calcularPrecio(self):
        for ingrediente in self.ingredientes:
            self.precio += ingrediente.precio

        return self.precio

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
