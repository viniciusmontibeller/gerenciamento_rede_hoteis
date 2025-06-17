from entidade.quarto_vip import QuartoVip
from limite.tela_quarto import TelaQuarto
from entidade.quarto import Quarto


class ControladorQuarto():

    def __init__(self, controlador_hotel):
        self.__controlador_hotel = controlador_hotel
        self.__tela_quarto = TelaQuarto()

    def adicionar(self):
        try: 
            codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
            dados_quarto = self.__tela_quarto.pega_dados_quarto()
            eh_quarto_vip = self.__tela_quarto.pega_eh_quarto_vip()

            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)
          
            hotel.adicionar_quarto(dados_quarto, eh_quarto_vip)
            
            self.__tela_quarto.mostra_mensagem("Quarto adicionado com sucesso!")
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def remover(self):
        try:
            codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
            self.listar(codigo_hotel)
            
            numero = self.__tela_quarto.pega_numero_quarto()
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)
            
            for reserva in self.__controlador_hotel.controlador_sistema.controlador_reserva.listar_reservas_por_hotel(codigo_hotel):
                if reserva.quarto.numero == numero:
                    raise Exception("Não é possível remover um quarto que ja possui reserva.")

            quarto_removido = hotel.remover_quarto(numero)
            if quarto_removido:
                self.__tela_quarto.mostra_mensagem("Removido com sucesso.")
            else:
                raise Exception(
                    f"Quarto com número [{numero}] não foi encontrado para ser removido."
                )
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def listar(self, codigo_hotel = None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
            
            lista_dados_quarto = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).listar_dados_quartos()
            
            self.__tela_quarto.mostrar_quartos(lista_dados_quarto)
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def alterar(self):
        codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
        self.listar(codigo_hotel)

        dados_quarto = self.__tela_quarto.pega_dados_quarto()

        try:
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)
            quarto_removido = hotel.remover_quarto(dados_quarto["numero"])
            if not quarto_removido:
                raise Exception(
                    f"Quarto de número [{dados_quarto['numero']}] não foi encontrado."
                )

            eh_quarto_vip = isinstance(quarto_removido, QuartoVip)
            hotel.adicionar_quarto(dados_quarto, eh_quarto_vip)
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def retornar(self):
        self.__controlador_hotel.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_quarto.tela_opcoes()]()
