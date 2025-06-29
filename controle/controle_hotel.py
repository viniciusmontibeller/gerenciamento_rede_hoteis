from controle.controle_cliente import ControladorCliente
from controle.controle_funcionario import ControladorFuncionario
from controle.controle_quarto import ControladorQuarto
from limite.tela_hotel import TelaHotel
from entidade.hotel import Hotel
from excecoes.lista_vazia_exception import ListaVaziaException
from excecoes.jah_existente_exception import JahExistenteException
from excecoes.nao_encontrado_exception import NaoEncontradoException
from persistence.hotel_dao import HotelDAO


class ControladorHotel():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_quarto = ControladorQuarto(self)
        self.__tela_hotel = TelaHotel()
        self.__hotel_dao = HotelDAO()

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_quarto(self):
        return self.__controlador_quarto

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def hotel_dao(self):
        return self.__hotel_dao

    def adicionar(self):
        dados_hotel = self.__tela_hotel.pega_dados_hotel()

        if dados_hotel is None:
            return

        try:
            if self.__hotel_dao.get(dados_hotel["codigo"]):
                raise JahExistenteException("Hotel", "hotel",
                                            dados_hotel["codigo"])
            self.__hotel_dao.add(
                Hotel(dados_hotel["nome"], dados_hotel["codigo"],
                      dados_hotel["logradouro"], dados_hotel["numero"],
                      dados_hotel["cidade"], dados_hotel["telefone"]))
            self.__tela_hotel.mostra_mensagem("Hotel adicionado com sucesso!")
        except JahExistenteException as e:
            self.__tela_hotel.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def remover(self):
        if not self.listar():
            return

        codigo = self.__tela_hotel.pega_codigo(" do hotel")
        
        if codigo is None:
            return

        try:
            self.__hotel_dao.remove(codigo)
            self.__tela_hotel.mostra_mensagem("Removido com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_hotel.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def listar(self):
        try:
            lista_hoteis = self.__hotel_dao.get_all()
            if not len(lista_hoteis) >= 1:
                raise ListaVaziaException('hoteis')
            lista_dados_hotel = list(
                map(
                    lambda hotel: {
                        "nome": hotel.nome,
                        "endereco": hotel.pegar_endereco(),
                        "codigo": hotel.codigo,
                        "telefone": hotel.telefone
                    }, lista_hoteis))

            self.__tela_hotel.mostrar_hoteis(lista_dados_hotel)
            return True
        except ListaVaziaException as e:
            self.__tela_hotel.mostra_mensagem(str(e))
            return False

    def alterar(self):
        if not self.listar():
            return

        dados_hotel = self.__tela_hotel.pega_dados_hotel()
        
        if dados_hotel is None:
            return

        try:
            hotel = self.__hotel_dao.get(dados_hotel["codigo"])

            hotel.nome = dados_hotel["nome"]
            hotel.telefone = dados_hotel["telefone"]
            hotel.mudar_endereco(dados_hotel["logradouro"],
                                 dados_hotel["numero"], dados_hotel["cidade"])

            self.__hotel_dao.update(hotel)

            self.__tela_hotel.mostra_mensagem("Alterado com sucesso.")
        except NaoEncontradoException as e:
            self.__tela_hotel.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        return self.__hotel_dao.get(codigo)

    def relatorio_geral(self):
        try:
            lista_dados_hoteis = []
            for hotel in self.__hotel_dao.get_all():
                lista_reservas = self.__controlador_sistema.controlador_reserva.listar_reservas_por_hotel(
                    hotel.codigo)

                lista_dados_hoteis.append({
                    "nome":
                    hotel.nome,
                    "codigo":
                    hotel.codigo,
                    "numero_funcionarios":
                    len(hotel.funcionarios),
                    "numero_clientes":
                    len(hotel.clientes),
                    "numero_quartos":
                    hotel.numero_de_quartos(),
                    "numero_reservas":
                    len(lista_reservas),
                    "faturamento_total_em_reservas":
                    sum(reserva.custo for reserva in lista_reservas)
                })

            self.__tela_hotel.mostra_relatorio(lista_dados_hoteis)
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def gerenciar_funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def gerenciar_clientes(self):
        self.__controlador_cliente.abre_tela()

    def gerenciar_quartos(self):
        self.__controlador_quarto.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.gerenciar_funcionarios,
            2: self.gerenciar_clientes,
            3: self.gerenciar_quartos,
            4: self.adicionar,
            5: self.alterar,
            6: self.listar,
            7: self.remover,
            8: self.relatorio_geral,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_hotel.tela_opcoes()]()
