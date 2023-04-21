from barberia import *
from barbero import *
from cliente import *

def iniciar():
    numero_sillas = int(input("Ingrese el numero de sillas disponibles en la barberia: "))
    barberia = Barberia(numero_sillas)

    while True:
        print("1. Agregar cliente")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            cliente = Cliente(nombre_cliente, barberia)
            cliente.start()

        elif opcion == 2:
            break
        else:
            print("Opcion invalida")
    
    print('Saliendo del programa...')
    time.sleep(2)