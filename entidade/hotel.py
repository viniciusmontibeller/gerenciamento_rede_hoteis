from entidade.quarto import Quarto
from entidade.quarto_vip import QuartoVip


class Hotel():

    def __init__(self, nome: str, codigo: int, endereco: str, telefone: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__endereco = endereco
        self.__telefone = telefone
        self.__quartos = []
        self.__funcionarios = []
        self.__clientes = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def funcionarios(self):
        return self.__funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios: list):
        if isinstance(funcionarios, list):
            self.__funcionarios = funcionarios

    @property
    def clientes(self):
        return self.__clientes

    @property
    def quartos(self):
        return self.__quartos
