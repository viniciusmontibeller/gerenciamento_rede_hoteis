from abc import ABC, abstractmethod
import datetime


class AbstractTela(ABC):

    def le_input_so_numero(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if not isinstance(valor_int, int):
                    raise ValueError
                return valor_lido
            except ValueError:
                print("Valor incorreto! Somente números")

    def le_input_int_com_range_de_validacao(self, mensagem: str, ints_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def le_input_so_int(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if not isinstance(valor_int, int):
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto! Somente números")

    def le_input_so_float(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_float = float(valor_lido)
                if not isinstance(valor_float, float):
                    raise ValueError
                return valor_float
            except ValueError:
                print("Valor incorreto! Somente números")

    def le_input_data(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                data = datetime.datetime.strptime(valor_lido, "%d-%m-%Y")
                return data
            except ValueError:
                print("Valor incorreto! Formato esperado: DD-MM-YYYY")

    def le_cpf(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if not isinstance(valor_int, int):
                    raise ValueError
                if len(valor_lido) != 11:
                    raise ValueError
                return valor_lido
            except ValueError:
                print("Valor incorreto! Formato esperado apenas números e exatamente 11 digitos.")

    def le_telefone(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if not isinstance(valor_int, int):
                    raise ValueError
                if len(valor_lido) != 11:
                    raise ValueError
                return valor_lido
            except ValueError:
                print("Valor incorreto! Formato esperado apenas números, exatamente 11 digitos e sem espaços.")
                print("Exemplo: 47988303706")

    @abstractmethod
    def tela_opcoes(self):
        pass
