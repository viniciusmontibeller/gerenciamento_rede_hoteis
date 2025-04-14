from quarto import Quarto
from quarto_normal import QuartoNormal
from quarto_vip import QuartoVip


class Hotel():

    def __init__(self, nome: str, codigo: int, endereco: str, telefone: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__endereco = endereco
        self.__telefone = telefone
        self.__quartos = []

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

    def adicionar_quarto(self, numero: int, capacidade: int,
                         preco_diaria: float, eh_vip: bool):
        if not any(quarto_existente.numero == numero
                   for quarto_existente in self.__hoteis):
            if eh_vip:
                self.__hoteis.append(
                    QuartoVip(numero, capacidade, preco_diaria))
            else:
                self.__hoteis.append(
                    QuartoNormal(numero, capacidade, preco_diaria))

    def remover_quarto(self, quarto: Quarto):
        if isinstance(quarto, Quarto):
            for quarto_existente in self.__quartos:
                if quarto_existente.numero == quarto.numero:
                    self.__quarto.remove(quarto_existente)

    def quartos_disponiveis(self):
        quartos_disponiveis = []
        for quarto in self.__quartos:
            if not quarto.reservado:
                quartos_disponiveis.append(quarto.numero)
        return quartos_disponiveis
