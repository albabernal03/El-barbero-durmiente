import threading
class Cliente(threading.Thread): #clase cliente, de tipo thread
    def __init__(self, nombre_cliente, barberia):
        threading.Thread.__init__(self)
        self.nombre_cliente = nombre_cliente
        self.barberia = barberia

    def run(self): #metodo run, que se ejecuta cuando se llama al metodo start, esto se usa para que el cliente entre a la barberia
        self.barberia.nuevo_cliente(self.nombre_cliente)