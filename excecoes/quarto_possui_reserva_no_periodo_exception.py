class QuartoPossuiReservaNoPeriodo(Exception):

    def __init__(self, data_entrada, data_saida):
        self.mensagem = f'Esse quarto ja possui reserva nesse periodo: de {data_entrada.strftime("%d-%m-%Y")} até {data_saida.strftime("%d-%m-%Y")}.'
        super().__init__(self.mensagem)
