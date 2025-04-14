from cliente import Cliente
from funcionario import Funcionario
from quarto import Quarto
from datetime import date
from status_reserva import StatusReserva


class Reserva():

    def __init__(self, codigo: int, cliente: Cliente, quarto: Quarto,
                 funcionario: Funcionario):
        self.__codigo = codigo
        self.__status = StatusReserva.AGENDADO
        self.__cliente = cliente
        self.__quarto = quarto
        self.__funcionario = funcionario
        self.__data_entrada = None
        self.__data_saida = None
        
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
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario
            
    def checkin(self):
        self.__status = StatusReserva.CHECKIN
        self.__data_entrada = date.today()

    def checkout(self):
        self.__data_saida = date.today()
        dias = self.__data_saida - self.__data_entrada
        self.__quarto.reservado = False
        self.__status = StatusReserva.FINALIZADO
        return self.__quarto.preco_diaria * dias

    def cancelar(self):
        self.__status = StatusReserva.CANCELADO

    def consultar_reserva(self):
        return f"Reserva de numero {self.__codigo} \n\
                Cliente {self.__cliente.nome}\n\
                Com inicio em {self.__data_entrada}\n\
                Status: {self.__status.value}\n\
                Duvias falar com {self.__funcionario.nome} por {self.__funcionario.telefone}\
                ou por {self.__funcionario.email}"


#testeReserva = Reserva(
    1, Cliente("w3123", "12312", "12312", "gads@gai.com"), Quarto(23, 2, 200),
    Funcionario("nome", "123", "123321", "asddas@gmailçcpom")

#print(testeReserva.consultar_reserva())
