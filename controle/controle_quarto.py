from entidade.quarto_vip import QuartoVip
from limite.tela_quarto import TelaQuarto
from entidade.quarto import Quarto
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_possui_reserva_exception import JahPossuiReservaException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from excecoes.jah_existente_exception import JahExistenteException


class ControladorQuarto():

    def __init__(self, controlador_hotel):
        self.__controlador_hotel = controlador_hotel
        self.__tela_quarto = TelaQuarto()

    def adicionar(self):
        try:
            if not len(self.__controlador_hotel.hotel_dao.get_all()) >= 1:
                raise Exception("Não existem hoteis cadastrados para incluir um quarto")
            
            codigo_hotel = self.__tela_quarto.pega_codigo(" do hotel")
            
            if codigo_hotel is None:
                return
            
            dados_quarto = self.__tela_quarto.pega_dados_quarto()
            
            if dados_quarto is None:
                return
            
            eh_quarto_vip = self.__tela_quarto.pega_eh_quarto_vip()
            
            if eh_quarto_vip is None:
                return

            hotel = self.__controlador_hotel.buscar_por_codigo(
                codigo_hotel)
            
            if hotel.busca_quarto_por_numero(dados_quarto["numero"]):
                raise JahExistenteException("quarto", "numero", dados_quarto["numero"])

            hotel.adicionar_quarto(dados_quarto, eh_quarto_vip)
            self.__controlador_hotel.hotel_dao.update(hotel)
            self.__tela_quarto.mostra_mensagem(
                "Quarto adicionado com sucesso!", "sucesso")
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e), "erro")

    def remover(self):
        codigo_hotel = self.__tela_quarto.pega_codigo(" do hotel")
        
        if codigo_hotel is None:
            return
        
        if not self.listar(codigo_hotel):
            return

        try:
            numero = self.__tela_quarto.pega_numero_quarto()
            
            if numero is None:
                return
            
            hotel = self.__controlador_hotel.buscar_por_codigo(
                codigo_hotel)

            for reserva in self.__controlador_hotel.controlador_sistema.controlador_reserva.listar_reservas_por_hotel(codigo_hotel):
                if reserva.quarto.numero == numero:
                    raise JahPossuiReservaException("quarto")

            quarto_removido = hotel.remover_quarto(numero)
            if quarto_removido:
                self.__controlador_hotel.hotel_dao.update(hotel)
                self.__tela_quarto.mostra_mensagem("Removido com sucesso.", "sucesso")
            else:
                raise NaoEncontradoException("quarto", "numero", numero)
        except JahPossuiReservaException as e:
            self.__tela_quarto.mostra_mensagem(str(e), "erro")
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e), "erro")

    def listar(self, codigo_hotel=None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_quarto.pega_codigo(" do hotel")
            if not len(self.__controlador_hotel.hotel_dao.get_all()) >= 1:
                raise Exception("Não existem hoteis cadastrados")
            if not len(self.__controlador_hotel.buscar_por_codigo(codigo_hotel).quartos) >= 1:
                raise ListaVaziaException('quartos')

            lista_dados_quarto = self.__controlador_hotel.buscar_por_codigo(
                codigo_hotel).listar_dados_quartos()

            self.__tela_quarto.mostrar_quartos(lista_dados_quarto)
            return True
        except Exception as e:
            self.__tela_quarto.mostra_mensagem(str(e))
        except ListaVaziaException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
            return False

    def alterar(self):
        codigo_hotel = self.__tela_quarto.pega_codigo(" do hotel")
        
        if codigo_hotel is None:
            return
        
        if not self.listar(codigo_hotel):
            return

        dados_quarto = self.__tela_quarto.pega_dados_quarto()
        
        if dados_quarto is None:
            return

        try:
            hotel = self.__controlador_hotel.buscar_por_codigo(
                codigo_hotel)
            quarto_removido = hotel.remover_quarto(dados_quarto["numero"])
            if not quarto_removido:
                raise NaoEncontradoException("quarto", "numero", dados_quarto["numero"])

            eh_quarto_vip = isinstance(quarto_removido, QuartoVip)
            hotel.adicionar_quarto(dados_quarto, eh_quarto_vip)
            self.__controlador_hotel.hotel_dao.update(hotel)
        except NaoEncontradoException as e:
            self.__tela_quarto.mostra_mensagem(str(e))
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
