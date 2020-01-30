from cliente import Cliente
from pizza import Pizza

class Pedido:

    def __init__(self, cliente, pizzas):
        self.cliente = cliente
        self.listaPizzas = list(pizzas)
        self.status = 'No entregado'

    def __init__(self, cliente):
        self.cliente = cliente
        self.status = 'No entregrado'
        self.listaPizzas = list()

    def calcularPrecio(self):
        self.precio = 0

        for pizza in self.listaPizzas:
            self.precio += pizza.calcularPrecio()

        return self.precio

    def finalizarEntrega(self):
        print('Se esta haciendo la entrega')
        self.status = 'Entregado'

    def agregarPizza(self, pizza):
        self.listaPizzas.append(pizza)
