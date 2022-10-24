

from Consola import Consola
from Scooter import Scooter
from Bicicleta import Bicicleta
from Tv import Tv
from Tecnologia import Tecnologia
from Transporte import Transporte


def registrartv():
    voltaje=int(input('ingresa el voltaje'))
    precio=float(input('ingresa el precio'))
    eficiencia=str(input('ingresa la eficiencia'))
    marca=str(input('ingresa la marca'))
    tamaño=float(input('ingresa el tamaño'))
    tv= Tv(voltaje,precio,eficiencia,marca,tamaño)
    listaTvs.append(tv)
    print('REGISTRADO')

    
def registrarConsola():
    voltaje=int(input('ingresa el voltaje: '))
    precio=float(input('ingresa el precio: '))
    eficiencia=input('ingresa la eficiencia: ')
    marca=input('ingresa la marca: ')
    nombreConsola=str(input('ingresa el nombre de la consola: '))
    version=str(input('ingresa la version: '))
    cs= Consola(voltaje,precio,eficiencia,marca,nombreConsola,version)
    listaConsolas.append(cs)
    print('REGISTRADO')

def registrarScooter():
    voltaje=int(input('ingresa el voltaje: '))
    precio=float(input('ingresa el precio: '))
    eficiencia=input('ingresa la eficiencia: ')
    marca=input('ingresa la marca: ')
    aro=input('ingresa el aro: ')
    velocidad=input('ingresa la velocidad: ')
    peso=input('ingresa el peso: ')
    sc= Scooter(voltaje,precio,eficiencia,marca,aro,velocidad,peso)
    listaScooters.append(sc)
    print('REGISTRADO')
    

def registrarBicicletas():
    aro=int(input('ingresa el aro: '))
    peso=float(input('ingresa el peso: '))
    precio=input('ingresa el precio: ')
    marca=input('ingresa la marca: ')

    b= Bicicleta(aro,peso,precio,marca)
    listaBicicletas.append(b)
    print('REGISTRADO')

def cotizartv():
    pass

def cotizarconsola():
    pass

def cotizarscooter():
    pass

def cotizarbicicleta():
    pass

listaTvs=[]
listaConsolas=[]
listaScooters=[]
listaBicicletas=[]



while True:
    print('Elige una OPCION: ')
    print('1-.Registrar Tv: ')
    print('2-.Registrar Consola: ')
    print('3-.Registrar Scooter: ')
    print('4-.Registrar Bicicletas: ')
    print('5-Cotizar Tv: ')
    print('6-Cotizar Consola: ')
    print('7-Cotizar Scooter: ')
    print('8-Cotizar Bicicleta: ')
    opcion=(input('elige una opcion '))
    if opcion == '1':
        registrartv()
       
    elif opcion == '2':
        registrarConsola()

    elif opcion == '3':
        registrarScooter()

    elif opcion == '4':
        registrarBicicletas()

    elif opcion == '5':
        cotizartv()

    elif opcion == '6':
        cotizarconsola()

    elif opcion == '7':
        cotizarscooter()

    elif opcion == '8':
        cotizarbicicleta()

    