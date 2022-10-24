from Transporte import Transporte

class Bicicleta(Transporte):


    def __init__(self,aro,peso,precio,marca):
        super().__init__()
        self.__aro=aro
        self.__peso=peso
        self.__precio=precio
        self.__marca=marca

    def get_aro(self):
        return self.__aro

    def get_peso(self):
        return self.__peso

    def get_precio(self):
        return self.__precio

    def get_marca(self):
        return self.__marca

    def set_aro(self,aro):
        self.__aro=aro
    
    def set_peso(self,peso):
        self.__peso=peso

    def set_precio(self,precio):
        self.__precio=precio

    def set_marca(self,marca):
        self.__marca=marca

    def calcularDespacho(self):
        despacho= self.__peso*400+super().get_despachoBase  
        print(f'el despacho del scooter es : {despacho}')