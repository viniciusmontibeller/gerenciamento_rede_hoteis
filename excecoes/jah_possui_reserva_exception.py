class JahPossuiReservaException(Exception):

    def __init__(self, nome):
        self.mensagem = f'\nNão é possível remover um {nome} que ja possui reserva.'
        super().__init__(self.mensagem)