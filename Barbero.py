import threading
class Barbero(threading.Thread): #clase barbero, de tipo thread
    def __init__(self, barberia):
        threading.Thread.__init__(self)
        self.barberia = barberia

    def run(self): #metodo run, que se ejecuta cuando se llama al metodo start, esto se usa para que el barbero entre a la barberia
        self.barberia.esperar_cliente()
