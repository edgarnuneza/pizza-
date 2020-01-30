class Cliente:
    """Clase del cliente"""

    def __init__(self, nombre, calle, numeroCasa, colonia):
        self.nombre = nombre
        self.calle = calle
        self.colonia = colonia
        self.numeroCasa = numeroCasa

    def hacerPedido(self):
        print('Haciendo pedido')