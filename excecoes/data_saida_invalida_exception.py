class DataSaidaInvalidaException(Exception):

    def __init__(self, data_entrada, campo_legivel):
        self.mensagem = f'A data de saída no {campo_legivel} não pode ser anterior à data de entrada ({data_entrada.strftime("%d-%m-%Y")}).'
        super().__init__(self.mensagem)
