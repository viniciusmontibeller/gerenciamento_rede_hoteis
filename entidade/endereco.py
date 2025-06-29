class Endereco:

    def __init__(self, logradouro: str, numero: int, cidade: str):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__cidade = cidade

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro: str):
        if isinstance(logradouro, str):
            self.__logradouro = logradouro

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade
