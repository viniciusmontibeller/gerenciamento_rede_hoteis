class DataSaidaInvalidaException(Exception):

    def __init__(self, data_entrada):
        self.mensagem = f'Reserva inválida. A data de saída deve ser após a data de entrada({data_entrada.strftime("%d-%m-%Y")}).'
        super().__init__(self.mensagem)
