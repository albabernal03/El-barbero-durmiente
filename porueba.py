#Problema del barbero durmiente con semaforos

import threading 
import time 
import random


class Barberia:
    def __init__(self,num_sillas):
        self.num_sillas = num_sillas
        self.mutex= threading.Lock() #semaforo para la barberia, esto es para que no entren mas de 1 cliente a la vez
        self.cliente = threading.Semaphore(0) #semaforo para el cliente, esto es para que el barbero no atienda a mas de 1 cliente a la vez
        self.barbero = threading.Semaphore(0) #semaforo para el barbero, esto es para que el barbero no atienda a mas de 1 cliente a la vez
        self.barbero_dormido= True

    def cortar_pelo(self):
        print("El barbero esta cortando el pelo")
        time.sleep(random.randit(1,5)) #tiempo que tarda en cortar el pelo
        print("El barbero termino de cortar el pelo")
        self.barbero.release() #libera al barbero para que pueda atender a otro cliente

    def esperar_nuevo_cliente(self):
        print("El barbero esta durmiendo...")
        self.cliente.acquire() #el acquires es para que el barbero no atienda a mas de 1 cliente a la vez
        print("El barbero esta atendiendo a un cliente")
        self.cortar_pelo() #llama a la funcion cortar_pelo

    def entrar_barberia(self):
        self.mutex.acquire()

        if self.barbero_dormido:
            self.barbero_dormido = False
            self.cliente.release()
            self.mutex.release()
            self.barbero.acquire()
        else:
            if self.num_sillas > 0:
                self.num_sillas -= 1
                self.cliente.release()
                self.mutex.release()
                self.barbero.acquire()
            else:
                self.mutex.release()
                print("No hay sillas disponibles, el cliente se va")
                time.sleep(1)
                self.entrar_barberia()

    def salir_barberia(self):
        self.mutex.acquire()
        self.num_sillas += 1
        self.mutex.release()

class Cliente:
    def __init__(self,barberia):
        self.barberia = barberia

    def run(self):
        self.barberia.entrar_barberia()
        self.barberia.salir_barberia()

class Barbero:
    def __init__(self,barberia):
        self.barberia = barberia

    def run(self):
        while True:
            self.barberia.esperar_nuevo_cliente()

            

