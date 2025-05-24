from abc import ABC, abstractmethod

class AbstractTela(ABC):
    
    @abstractmethod
    def le_input_int(self, mensagem: str, ints_validos: list = None):
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
    
    @abstractmethod
    def le_input_so_numero(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                if not isinstance(valor_lido, int):
                    raise ValueError
                return str(valor_lido)
            except ValueError:
                print("Valor incorreto! Somente números")
                
    @abstractmethod
    def tela_opcoes(self):
        pass