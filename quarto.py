

class Quarto():
    
    def __init__(self, numero: int, capacidade: int, preco_diaria: float):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__preco_diaria = preco_diaria
        self.__ocupado = False
        
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
            
    @property
    def preco_diaria(self):
        return self.__preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self, preco_diaria: float):
        if isinstance(preco_diaria, float):
            self.__preco_diaria = preco_diaria
            
    def checkin(self):
        self.__ocupado = True
        
    def checkout(self):
        self.__ocupado = False