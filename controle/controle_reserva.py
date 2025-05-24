from controle_sistema import ControladorSistema
from limite.tela_reserva import TelaReserva


class ConroladorReserva():

    def __init__(self, controlador_sistema: ControladorSistema):
        self.__reservas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
