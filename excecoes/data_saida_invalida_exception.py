class DataSaidaInvalidaException(Exception):

    def __init__(self, data_entrada):
        self.mensagem = f'A data de saída não pode ser anterior à data de entrada ({data_entrada.strftime("%d-%m-%Y")}13).'
        super().__init__(self.mensagem)
