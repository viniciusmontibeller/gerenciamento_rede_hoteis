from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.jah_possui_reserva_exception import JahPossuiReservaException
from excecoes.nao_encontrado_exception import NaoEncontradoException


class ControladorFuncionario():

    def __init__(self, controlador_hotel):
        self.__controlador_hotel = controlador_hotel
        self.__tela_funcionario = TelaFuncionario()

    def adicionar(self):
        try:
            codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
            dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(
                codigo_hotel)

            if self.busca_por_cpf(hotel, dados_funcionario["cpf"]):
                raise JahExistenteException("Funcionario", "CPF", dados_funcionario["cpf"])
            novo_funcionario = Funcionario(dados_funcionario["nome"],
                            dados_funcionario["cpf"],
                            dados_funcionario["telefone"],
                            dados_funcionario["email"])
            hotel.adicionar_funcionario(novo_funcionario)
            self.__tela_funcionario.mostra_mensagem(
                "Funcionario adicionado com sucesso!")
        except JahExistenteException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def remover(self):
        codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
        if not self.listar(codigo_hotel):
            return

        cpf = self.__tela_funcionario.pega_cpf_funcionario()

        try:
            funcionario_existe = False
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)

            for funcionario in hotel.funcionarios:
                if funcionario.cpf == cpf:
                    for reserva in self.__controlador_hotel.controlador_sistema.controlador_reserva.listar_reservas_por_hotel(codigo_hotel):
                        if reserva.funcionario.cpf == cpf:
                            raise JahPossuiReservaException("funcionario")
                    hotel.remover_funcionario(cpf)
                    self.__tela_funcionario.mostra_mensagem(
                        "Removido com sucesso.")
                    funcionario_existe = True
                    break

            if not funcionario_existe:
                raise NaoEncontradoException("Funcionario", "CPF", cpf)
        except JahPossuiReservaException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
        except NaoEncontradoException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def listar(self, codigo_hotel=None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
                
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)
                
            if not len(hotel.funcionarios) >= 1:
                raise ListaVaziaException('funcionarios')


            lista_dados_funcionario = map(
                lambda funcionario: {
                    "nome": funcionario.nome,
                    "cpf": funcionario.cpf,
                    "telefone": funcionario.telefone,
                    "email": funcionario.email
                }, hotel.funcionarios)

            self.__tela_funcionario.mostrar_funcionarios(
                lista_dados_funcionario)
            return True
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
        except ListaVaziaException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
            return False

    def alterar(self):
        codigo_hotel = self.__tela_funcionario.pega_codigo_hotel()
        if not self.listar(codigo_hotel):
            return

        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()

        try:
            funcionario_existe = False

            for funcionario in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).funcionarios:
                if funcionario.cpf == dados_funcionario["cpf"]:
                    funcionario.nome = dados_funcionario["nome"]
                    funcionario.telefone = dados_funcionario["telefone"]
                    funcionario.email = dados_funcionario["email"]
                    self.__tela_funcionario.mostra_mensagem(
                        "Alterado com sucesso.")
                    funcionario_existe = True
                    break

            if not funcionario_existe:
                raise NaoEncontradoException("Funcionario", "CPF", dados_funcionario["cpf"])
        except NaoEncontradoException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_funcionario.mostra_mensagem(str(e))

    def busca_por_cpf(self, hotel, cpf):
        for funcionario in hotel.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario

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
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()
