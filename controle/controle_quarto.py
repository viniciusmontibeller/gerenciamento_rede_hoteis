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
            quarto = None
            if eh_quarto_vip:
                quarto = QuartoVip(dados_quarto["numero"],
                        dados_quarto["capacidade"],
                        dados_quarto["preco_diaria"])
            else:
                quarto = Quarto(dados_quarto["numero"],
                        dados_quarto["capacidade"],
                        dados_quarto["preco_diaria"])

            hotel.quartos.append(quarto)
            
            self.__tela_quarto.mostra_mensagem("Quarto adicionado com sucesso!")
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def remover(self):
        codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
        numero = self.__tela_quarto.pega_numero_quarto()
        try:
            quarto_existe = False
            for quarto in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).quartos:
                if quarto.numero == numero:
                    self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).quartos.remove(quarto)
                    self.__tela_quarto.mostra_mensagem("Removido com sucesso.")
                    quarto_existe = True
                    break

            if not quarto_existe:
                raise Exception(
                    f"Quarto com número [{numero}] não foi encontrado para ser removido."
                )
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def listar(self, codigo_hotel = None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
            
            lista_dados_quarto = map(
                lambda quarto: {
                    "numero": quarto.numero,
                    "capacidade": quarto.capacidade,
                    "preco_diaria": quarto.preco_diaria
                }, self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).quartos)
            
            self.__tela_quarto.mostrar_quartos(lista_dados_quarto)
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def alterar(self):
        codigo_hotel = self.__tela_quarto.pega_codigo_hotel()
        self.listar(codigo_hotel)

        dados_quarto = self.__tela_quarto.pega_dados_quarto()

        try:
            quarto_existe = False
            for quarto in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).quartos:
                if quarto.numero == dados_quarto["numero"]:
                    quarto.capacidade = dados_quarto["capacidade"]
                    quarto.preco_diaria = dados_quarto["preco_diaria"]
                    self.__tela_quarto.mostra_mensagem("Alterado com sucesso.")
                    quarto_existe = True
                    break

            if not quarto_existe:
                raise Exception(
                    f"Quarto de número [{dados_quarto['numero']}] não foi encontrado."
                )
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))

    def busca_por_numero(self, hotel, numero):
        for quarto in hotel.quartos:
            if quarto.numero == numero:
                return quarto

        return None

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
