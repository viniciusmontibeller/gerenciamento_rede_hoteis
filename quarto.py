class Quarto():

    def __init__(self, numero: int, capacidade: int, preco_diaria: float):
        self.__numero = numero
        self.__capacidade = capacidade
        self.__preco_diaria = preco_diaria
        self.__reservado = False

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

    @property
    def reservado(self):
        return self.__reservado
    
    @reservado.setter
    def reservado(self, reservado: bool):
        if isinstance(reservado, bool):
            self.__reservado = reservado
            
    def calcular_taxa_servico(self):
        return self.__preco_diaria
