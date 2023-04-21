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

        