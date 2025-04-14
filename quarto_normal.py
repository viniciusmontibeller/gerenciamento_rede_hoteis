from quarto import Quarto


class QuartoNormal(Quarto):

    def __init__(self, numero: int, capacidade: int, preco_diaria: float):
        super().__init__(numero, capacidade, preco_diaria)

    def calcular_taxa_servico(self):
        return super().calcular_taxa_servico() * 1.10