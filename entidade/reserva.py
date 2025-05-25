from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from entidade.hotel import Hotel
from entidade.quarto import Quarto
from datetime import date
from entidade.status_reserva import StatusReserva


class Reserva():

    def __init__(self, codigo: int, cliente: Cliente, hotel: Hotel, quarto: Quarto,
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

        self.__quarto.reservado = True

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
        if self.__status is not StatusReserva.FINALIZADO:
            raise Exception(
                "Não é possível ver o custo de uma reserva que ainda não foi finalizada."
            )

        return self.__custo

    def checkin(self):
        self.__status = StatusReserva.CHECKIN
        self.__data_entrada = date.today()

    def checkout(self):
        self.__data_saida = date.today()
        self.__quarto.reservado = False
        self.__status = StatusReserva.FINALIZADO

        dias = (self.__data_saida - self.__data_entrada).days
        self.__custo = self.__quarto.preco_diaria * dias
        if self.__cliente.fidelidade:
            self.__custo = self.__custo * 0.90

    def cancelar(self):
        self.__status = StatusReserva.CANCELADO

    def consultar_reserva(self):
        inicio = f"Com início em {self.__data_entrada}\n" if self.__data_entrada else ""
        saida = f"Com saída em {self.__data_saida}\n" if self.__data_saida else ""
        return (
            f"Reserva de numero {self.__codigo}\n"
            f"Cliente {self.__cliente.nome}\n"
            f"{inicio}"
            f"{saida}"
            f"Status: {self.__status.value}\n"
            f"Duvidas falar com {self.__funcionario.nome} por {self.__funcionario.telefone} "
            f"ou por {self.__funcionario.email}")
