from typing import List
from entidade.hotel import Hotel


class Rede():

    def __init__(self, nome: str, codigo: int, localizacao_rede: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__localizacao_rede = localizacao_rede
        self.__hoteis: List[Hotel] = []

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
    def localizacao_rede(self):
        return self.__localizacao_rede

    @localizacao_rede.setter
    def localizacao_rede(self, localizacao_rede: str):
        if isinstance(localizacao_rede, str):
            self.__localizacao_rede = localizacao_rede

    @property
    def hoteis(self):
        return self.__hoteis

    def adicionar_hotel(self, hotel: Hotel):
        if isinstance(hotel, Hotel):
            if not any(hotel_existente.codigo == hotel.codigo
                       for hotel_existente in self.__hoteis):
                self.__hoteis.append(hotel)
                return hotel

    def remover_hotel(self, codigo: int):
        for hotel in self.__hoteis:
            if hotel.codigo == codigo:
                self.__hoteis.remove(hotel)
                return hotel

        return None
