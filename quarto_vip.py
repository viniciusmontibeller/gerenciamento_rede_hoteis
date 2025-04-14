from quarto import Quarto


class QuartoVip(Quarto):

    def __init__(self, numero: int, capacidade: int, preco_diaria: float):
        super().__init__(numero, capacidade, preco_diaria)
