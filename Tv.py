from tkinter import N
from Tecnologia import Tecnologia



class Tv(Tecnologia):
    

    def __init__(self, voltaje, precio, eficiencia, marca,tamanio):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamanio=tamanio

    def get_tamanio(self):
        return self.__tamanio
    
    def set_tamanio(self,tamanio):
        self.__tamanio=tamanio


        
    def imprimirtv(self):
        print(f"VOLTAJE: {self.__voltaje}, PRECIO:{self.__precio},EFICIENCIA:{self.__eficiencia},MARCA:{self.__marca},TAMANIO: {self.__tamanio}")
        x=super().calcularDescuento
        total=1
        print(f"DESCUENTO APLICADO{x},VALOR TOTAL:")

    def __str__(self) -> str:
        return f'{super().__str__()}tamaño : {self.__tamanio}'
