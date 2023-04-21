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
        print("El barbero esta durmiendo")
        self.cliente.acquire() #el acquires es para que el barbero no atienda a mas de 1 cliente a la vez