class Cliente:
    def __init__(self, nombre, email, direccion, saldo_inicial):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.saldo = saldo_inicial

    def realizar_compra(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"{self.nombre} realizó una compra de ${monto}. Saldo restante: ${self.saldo}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para realizar la compra.")

    def hacer_devolucion(self, monto):
        self.saldo += monto
        print(f"{self.nombre} hizo una devolución de ${monto}. Saldo actual: ${self.saldo}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Saldo: ${self.saldo}"