from cliente import Cliente
from ingrediente import Ingrediente

class Datos:

    def __init__(self):
        self.listaClientes = list()
        self.listaIngredientes = list()
        self.cargarDatosClientes()
        self.cargarDatosIngredientes()

    def cargarDatosClientes(self):
        self.listaClientes.append(Cliente('Juan', 'Revolucion', 35, 'Independencia'))
        self.listaClientes.append(Cliente('Pedro', 'Reforma', 35, 'Madero'))
        self.listaClientes.append(Cliente('Maria', 'Samalayuca', 35, 'Monterrey'))

    def cargarDatosIngredientes(self):
        self.listaIngredientes.append(Ingrediente('Peperoni', 50))
        self.listaIngredientes.append(Ingrediente('Piña', 35))

    def mostrarClientes(self):
        i = 1
        for cliente in self.listaClientes:
            print(i, cliente.nombre, cliente.calle, cliente.colonia)
            i += 1

    def mostrarIngredientes(self):
        i = 1
        for ingrediente in self.listaIngredientes:
            print(i, ingrediente.nombre, ingrediente.precio)
            i += 1

    def añadirCliente(self):
        nombre = input('Ingresa el nombre\n')
        calle = input('Ingresa la calle\n')
        colonia = input('Ingresa la colonia\n')
        numero = input('Ingresa el numero de casa\n')

        cliente = Cliente(nombre, calle, numero, colonia)
        self.listaClientes.append(cliente)

        return cliente

    def añadirIngrediente(self):
        self.nombre = input('Ingresa el nombre del ingrediente\n')
        self.precio = int(input('Ingresa el precio del ingrediente\n'))

        ingrediente = Ingrediente(self.nombre, self.precio)
        self.listaIngredientes.append(ingrediente)

        return ingrediente



