from cliente import Cliente
from funcionario import Funcionario
from quarto import Quarto
from datetime import date


class Reserva():
    
    def __init__(self, codigo: int, cliente: Cliente, quarto: Quarto, funcionario: Funcionario):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__quarto = quarto
        self.__funcionario = funcionario
        self.__ativa = True
        self.__data_entrada = date.today()
        self.__data_saida = None
        
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
            
    def calcular_valor_total(self):
        self.__data_saida = date.today()
        dias = self.__data_saida - self.__data_entrada
        return self.__quarto.preco_diaria * dias
    
    def cancelar(self):
        self.__ativa = False
        
    def consultar_reserva(self):
        ehAtiva = "Ativa" if self.__ativa else "Inativa"
        return f"Reserva de numero {self.__codigo}\
                Cliente {self.__cliente.nome}\
                Com inicio em {self.__data_entrada}\
                Esta {ehAtiva}"