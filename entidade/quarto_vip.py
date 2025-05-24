from quarto import Quarto


class QuartoVip(Quarto):

    def _init_(self, numero: int, capacidade: int, preco_diaria: float):
        super()._init_(numero, capacidade, preco_diaria)

        taxa_de_servico: float = 1.20
        self._preco_diaria = self._preco_diaria * taxa_de_servico
