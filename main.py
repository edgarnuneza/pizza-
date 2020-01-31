from pedido import Pedido
from pizza import Pizza
from cliente import Cliente
from ingrediente import Ingrediente
from datos import Datos


def opcionIngredientes():
    opcion = 1

    while opcion == 1:
        print('Desa agregar ingredientes')
        print('1.- si')
        print('2. no')

        opcion = int(input())

        if not opcion == 1:
            break

        datos.mostrarIngredientes()
        print(datos.listaIngredientes.__len__() + 1, 'Crear un nuevo ingrediente')
        numeroIngrediente = int(input('Selecciona un ingrediente \n'))

        if numeroIngrediente == datos.listaIngredientes.__len__() + 1:
            ingrediente = datos.añadirIngrediente()
        else:
            ingrediente = datos.listaIngredientes[numeroIngrediente - 1]

        print(ingrediente.nombre, ingrediente.precio)

        pizza.agregarIngrediente(ingrediente)

def opcionPizzas():
    tamaño = input('Ingresa el tamaño de la pizza\n')
    precio = int(input('Ingresa el precio\n'))

    return Pizza(tamaño, precio)

print('1.- Hacer un pedido')
print('2.- Salir')

opcion = int(input('Elige una opcion\n'))

if opcion == 1:
    datos = Datos()
    datos.mostrarClientes()
    print(datos.listaClientes.__len__() + 1, 'Añadir un nuevo cliente')

    numeroCliente = int(input('Selecciona un cliente\n'))

    if numeroCliente == datos.listaClientes.__len__() + 1:
        cliente = datos.añadirCliente()

    else:
        cliente = datos.listaClientes[numeroCliente - 1]

    pedido = Pedido(cliente)

    opcionPizza = 1

    while opcionPizza == 1:
        print('Elige una opcion')
        print('1.- Agregar una pizza')
        print('2.- Terminar compra')

        opcionPizza = int(input())

        if not opcionPizza == 1:
            break

        pizza = opcionPizzas()
        opcionIngredientes()
        pizza.preparar()
        pizza.empaquetar()
        pedido.agregarPizza(pizza)


print('El precio del pedido de ', cliente.nombre, ' es ', pedido.calcularPrecio())
pedido.finalizarEntrega()