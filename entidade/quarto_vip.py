from entidade.quarto import Quarto


class QuartoVip(Quarto):

    def __init__(self, numero: int, capacidade: int, preco_diaria: float):
        super().__init__(numero, capacidade, preco_diaria)

        taxa_de_servico: float = 1.20
        self.preco_diaria = self.preco_diaria * taxa_de_servico
