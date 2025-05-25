from limite.tela_reserva import TelaReserva


class ControladorReserva():

    def __init__(self, controlador_sistema):
        self.__reservas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.buscar,
            5: self.remover,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_reserva.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()    