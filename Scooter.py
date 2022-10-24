from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Transporte,Tecnologia):
    
    def __init__(self, voltaje, precio, eficiencia, marca, despachoBase,aro, velocidad, peso ):
        Tecnologia.__init__(voltaje,precio,eficiencia,marca)
        Transporte.__init__(despachoBase)
        self.__aro=aro
        self.__velocidad=velocidad
        self.__peso=peso

    def get_aro(self):
        return self.__aro

    def get_velocidad(self):
        return self.__velocidad

    def get_peso(self):
        return self.__peso
        
    
    def set_aro(self,aro):
        self.__aro=aro

    def set_velocidad(self,velocidad):
        self.__velocidad=velocidad

    def set_peso(self,peso):
        self.__peso=peso

    def calcularDespacho(self):
        despacho= self.__peso*300+super().get_despachoBase
        print(f'el despacho del scooter es : {despacho}')

            
    def imprimirConsola(self):
        print(f"VOLTAJE: {self.__voltaje}, PRECIO:{self.__precio},EFICIENCIA:{self.__eficiencia},MARCA:{self.__marca},ARO: {self.__aro},VELOCIDAD:{self.__velocidad},PESO:{self.__peso}")
        x=super().calcularDescuento
        print(f"DESCUENTO APLICADO{x},VALOR TOTAL:")

    def __str__(self) -> str:
         return f'{super().__str__()}aro : {self.__aro}, velocidad: {self.__velocidad} peso: {self.__peso}'