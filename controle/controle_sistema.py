from controle.controle_rede import ControladorRede
from controle.controle_reserva import ControladorReserva
from controle.controle_hotel import ControladorHotel
from limite.tela_sistema import TelaSistema


class ControladorSistema():
    __instance = None

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_rede = ControladorRede(self)
        self.__controlador_hotel = ControladorHotel(self)
        self.__controlador_reserva = ControladorReserva(self)

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    @property
    def controlador_rede(self):
        return self.__controlador_rede

    @property
    def controlador_reserva(self):
        return self.__controlador_reserva

    @property
    def controlador_hotel(self):
        return self.__controlador_hotel

    def inicializar_sistema(self):
        self.abre_tela()

    def abre_tela_rede(self):
        self.controlador_rede.abre_tela()

    def abre_tela_hotel(self):
        self.controlador_hotel.abre_tela()

    def abre_tela_reserva(self):
        self.controlador_reserva.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.abre_tela_rede,
            2: self.abre_tela_hotel,
            3: self.abre_tela_reserva,
            0: self.encerrar_sistema
        }

        while True:
            opcao_selecionada = self.__tela_sistema.tela_opcoes()
            funcao_selecionada = lista_opcoes[int(opcao_selecionada)]
            funcao_selecionada()
