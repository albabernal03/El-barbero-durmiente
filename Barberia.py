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

    def cortar_pelo(self):
        print("El barbero esta cortando el pelo...")
        time.sleep(random.randint(1,5)) #tiempo que tarda en cortar el pelo
        print("El barbero termino de cortar el pelo")

    def esperar_cliente(self):
        print("El barbero esta durmiendo")
        while True:
            self.barbero.acquire() #el barbero espera a que el cliente se siente en la silla, el acquire se usa que el semaforo se ponga en 0
            self.mutex.acquire() #el barbero adquiere el mutex para que no se pueda acceder a la barberia
            self.clientes_en_silla-=1 #el barbero atiende al cliente, por lo que hay un cliente menos en la barberia
            self.mutex.release() #el barbero libera el mutex para que otro cliente pueda entrar a la barberia
            self.cliente.release() #el barbero libera el semaforo del cliente para que este pueda salir de la barberia
            self.cortar_pelo() #el barbero corta el pelo

    def nuevo_cliente(self, nombre_cliente):
        print(f'El cliente {nombre_cliente} llego a la barberia')
        self.mutex.acquire() #el cliente adquiere el mutex para que no se pueda acceder a la barberia
        if self.clientes_en_silla < self.numero_sillas: #si hay sillas disponibles
            self.clientes_en_silla+=1 #el cliente se sienta en la silla
            if self.barbero_dur:
                self.barbero_dur = False
                self.barbero.release() #el cliente libera el semaforo del barbero para que este deje de dormir
            self.mutex.release() #el cliente libera el mutex para que otro cliente pueda entrar a la barberia
            self.cliente.acquire() #el cliente espera a que el barbero lo atienda, el acquire se usa que el semaforo se ponga en 0
            print(f'El cliente {nombre_cliente} se esta cortando el pelo')
        else: #si no hay sillas disponibles
            print(f'El cliente {nombre_cliente} se fue porque no habia sillas disponibles')
            self.mutex.release() #el cliente libera el mutex para que otro cliente pueda entrar a la barberia
