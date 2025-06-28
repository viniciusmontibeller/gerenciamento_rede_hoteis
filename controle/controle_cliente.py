from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from persistence.hotel_dao import HotelDAO
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from excecoes.jah_possui_reserva_exception import JahPossuiReservaException


class ControladorCliente():

    def __init__(self, controlador_hotel):
        self.__controlador_hotel = controlador_hotel
        self.__tela_cliente = TelaCliente()

    def adicionar(self):
        try:
            if not len(self.__controlador_hotel.hotel_dao.get_all()) >= 1:
                raise Exception(
                    "Não existem hoteis cadastrados para incluir um cliente")

            codigo_hotel = self.__tela_cliente.pega_codigo(" do hotel")
            dados_cliente = self.__tela_cliente.pega_dados_cliente()
            hotel = self.__controlador_hotel.buscar_por_codigo(codigo_hotel)

            if hotel.busca_cliente_por_cpf(dados_cliente["cpf"]):
                raise JahExistenteException("Cliente", "CPF",
                                            dados_cliente["cpf"])
            novo_cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"],
                                   dados_cliente["telefone"],
                                   dados_cliente["email"])
            hotel.adicionar_cliente(novo_cliente)
            self.__controlador_hotel.hotel_dao.update(hotel)
            self.__tela_cliente.mostra_mensagem(
                "Cliente adicionado com sucesso!")
        except JahExistenteException as e:
            self.__tela_cliente.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))

    def remover(self):
        codigo_hotel = self.__tela_cliente.pega_codigo(" do hotel")
        if not self.listar(codigo_hotel):
            return

        cpf = self.__tela_cliente.pega_cpf()

        try:
            cliente_existe = False
            hotel = self.__controlador_hotel.buscar_por_codigo(codigo_hotel)

            if hotel.busca_cliente_por_cpf(cpf):
                for reserva in self.__controlador_hotel.controlador_sistema.controlador_reserva.listar_reservas_por_hotel(
                        codigo_hotel):
                    if reserva.cliente.cpf == cpf:
                        raise JahPossuiReservaException("cliente")

                hotel.remover_cliente(cpf)
                self.__controlador_hotel.hotel_dao.update(hotel)
                self.__tela_cliente.mostra_mensagem("Removido com sucesso.")
                cliente_existe = True

            if not cliente_existe:
                raise NaoEncontradoException("Cliente", "CPF", cpf)
        except JahPossuiReservaException as e:
            self.__tela_cliente.mostra_mensagem(str(e))
        except NaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))

    def listar(self, codigo_hotel=None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_cliente.pega_codigo(" do hotel")

            if not len(self.__controlador_hotel.hotel_dao.get_all()) >= 1:
                raise Exception("Não existem hoteis cadastrados")
            if not len(
                    self.__controlador_hotel.buscar_por_codigo(
                        codigo_hotel).clientes) >= 1:
                raise ListaVaziaException('clientes')

            lista_dados_cliente = self.__controlador_hotel.buscar_por_codigo(
                codigo_hotel).listar_dados_clientes()

            self.__tela_cliente.mostrar_clientes(lista_dados_cliente)
            return True
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))
        except ListaVaziaException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
            return False

    def alterar(self):
        codigo_hotel = self.__tela_cliente.pega_codigo(" do hotel")
        if not self.listar(codigo_hotel):
            return

        dados_cliente = self.__tela_cliente.pega_dados_cliente()

        try:
            cliente_existe = False

            hotel = self.__controlador_hotel.buscar_por_codigo(codigo_hotel)

            cliente = hotel.busca_cliente_por_cpf(dados_cliente["cpf"])
            if cliente:
                cliente.nome = dados_cliente["nome"]
                cliente.telefone = dados_cliente["telefone"]
                cliente.email = dados_cliente["email"]
                self.__controlador_hotel.hotel_dao.update(hotel)
                self.__tela_cliente.mostra_mensagem("Alterado com sucesso.")
                cliente_existe = True

            if not cliente_existe:
                raise NaoEncontradoException("cliente", "CPF",
                                             dados_cliente["cpf"])
        except NaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))

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
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
