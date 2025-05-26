from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from entidade.hotel import Hotel
from entidade.quarto import Quarto
from datetime import date
from entidade.status_reserva import StatusReserva


class Reserva():

    def __init__(self, codigo: int, hotel: Hotel, quarto: Quarto, cliente: Cliente,
                 funcionario: Funcionario, data_entrada: date, data_saida: date):
        self.__codigo = codigo
        self.__status = StatusReserva.AGENDADO
        self.__cliente = cliente
        self.__hotel = hotel
        self.__quarto = quarto
        self.__funcionario = funcionario
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida
        self.__custo = 0

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def quarto(self):
        return self.__quarto

    @quarto.setter
    def quarto(self, quarto: Quarto):
        if isinstance(quarto, Quarto):
            self.__quarto = quarto

    @property
    def hotel(self):
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: Hotel):
        if isinstance(hotel, Hotel):
            self.__hotel = hotel

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo: float):
        if isinstance(custo, float):
            self.__custo = custo

    @property
    def data_entrada(self):
        return self.__data_entrada

    @data_entrada.setter
    def data_entrada(self, data_entrada: date):
        if isinstance(data_entrada, date):
            self.__data_entrada = data_entrada

    @property
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, data_saida: date):
        if isinstance(data_saida, date):
            self.__data_saida = data_saida

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: StatusReserva):
        if isinstance(status, StatusReserva):
          self.__status = status
