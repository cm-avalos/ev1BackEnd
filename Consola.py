from Tecnologia import Tecnologia


class Consola(Tecnologia):
    
    def __init__(self, voltaje, precio, eficiencia, marca,nombreConsola,version):
        super().__init__(voltaje, precio, eficiencia, marca)

        self.__nombreConsola=nombreConsola
        self.__version=version

    def get_nombreConsola(self):
        return self.__nombreConsola

    def set_nombreConsola(self,nombreConsola):
        self.__nombreConsola=nombreConsola

    def calcularDescuento(self):
        

         if self.__version=='LITE'or self.__version=='lite':   
                descuento1=self.__precio*0.05
                print(f'Descuento Consola: {descuento1}')               
         else:('No Hay descuentos')


    def imprimirConsola(self,):
        print(f"VOLTAJE: {self.__voltaje}, PRECIO:{self.__precio},EFICIENCIA:{self.__eficiencia},MARCA:{self.__marca},nombreConsola: {self.__nombreConsola},VERSION : {self.__version}")
        x=super().calcularDescuento        
        print(f"DESCUENTO APLICADO{x},VALOR TOTAL:")


    def __str__(self) -> str:
        return f'{super().__str__()}nombre consola : {self.__nombreConsola} version:{self.__version}'