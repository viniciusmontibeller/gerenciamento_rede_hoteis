from limite.tela_reserva import TelaReserva


class ControladorReserva():

    def __init__(self, controlador_sistema):
        self.__reservas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
