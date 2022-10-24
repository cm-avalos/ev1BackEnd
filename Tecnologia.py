class Tecnologia:


    def __init__(self,voltaje,precio,eficiencia,marca):
        self.__voltaje=voltaje
        self.__precio=precio
        self.__eficiencia=eficiencia
        self.__marca=marca

    #get
    def get_voltaje(self):
            return self.__voltaje

    def get_precio(self):
            return self.__precio

    def get_eficiencia(self):
            return self.__eficiencia

    def get_marca(self):
            return self.__marca

    #set

    def set_voltaje(self,voltaje):
        self.__voltaje=voltaje

    def set_precio(self,precio):
        self.__precio=precio

    def set_eficiencia(self,eficiencia):
        self.__eficiencia=eficiencia

    def set_marca(self,marca):
        self.__marca=marca

    #funciones  
    def calcularDescuento(self):
            if self.__eficiencia =='A' or self.__eficiencia=='B' or self.__eficiencia=='a' or self.__eficiencia=='b':   
                descuento1=self.__precio*0.5
                print(f'Descuento: {descuento1}')

            elif self.__eficiencia =='C' or self.__eficiencia=='c' or self.__eficiencia=='d' or self.__eficiencia=='D':
                descuento2= self.__precio*0.3
                print(f'Descuento: {descuento2} ')

            elif self.__eficiencia == self.__eficiencia =='E' or self.__eficiencia=='e' or self.__eficiencia=='F' or self.__eficiencia=='f':
                descuento3=self.__precio*0.1
                print(f'Descuento: {descuento3} ')
            
            else:
                ('No Hay descuentos')

    
