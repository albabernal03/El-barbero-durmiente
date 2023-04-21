#Problema del barbero durmiente con semaforos

import threading 
import time 
import random

class Barberia:
    def __init__(self, numero_sillas):
        self.numero_sillas = numero_sillas
        self.clientes_en_silla=0 
        self.mutex = threading.Lock() #semaforo para la barberia, el lock es para que no se pueda acceder a la barberia si esta ocupada
        self.cliente= threading.Semaphore(0) #semaforo para el cliente, el semaforo es para que el cliente espere a que el barbero lo atienda
        self.barbero= threading.Semaphore(0) #semaforo para el barbero, el semaforo es para que el barbero espere a que el cliente se siente en la silla
        self.barbero_dur= True #variable para saber si el barbero esta durmiendo o no




