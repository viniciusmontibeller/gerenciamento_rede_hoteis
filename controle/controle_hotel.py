from controle.controle_cliente import ControladorCliente
from controle.controle_funcionario import ControladorFuncionario
from controle.controle_quarto import ControladorQuarto
from limite.tela_hotel import TelaHotel
from entidade.hotel import Hotel
from excecoes.lista_vazia_exception import ListaVaziaException


class ControladorHotel():

    def __init__(self, controlador_sistema):
        self.__hoteis = []
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_quarto = ControladorQuarto(self)
        self.__tela_hotel = TelaHotel()

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
    def hoteis(self):
        return self.__hoteis

    def busca_hotel_por_codigo(self, codigo):
        for hotel in self.__hoteis:
            if hotel.codigo == codigo:
                return hotel
        raise Exception(f"Hotel de código [{codigo}] não foi encontrado.")

    def adicionar(self):
        dados_hotel = self.__tela_hotel.pega_dados_hotel()
        try:
            if self.buscar_por_codigo(dados_hotel["codigo"]):
                raise Exception("Hotel ja existente")
            self.__hoteis.append(
                Hotel(dados_hotel["nome"], dados_hotel["codigo"],
                      dados_hotel["endereco"], dados_hotel["telefone"]))
            self.__tela_hotel.mostra_mensagem("Hotel adicionado com sucesso!")
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def remover(self):
        if not self.listar():
            return

        codigo = self.__tela_hotel.pega_codigo_hotel()
        
        try:
            hotel_existe = False
            for hotel in self.__hoteis:
                if hotel.codigo == codigo:
                    self.__hoteis.remove(hotel)
                    self.__tela_hotel.mostra_mensagem("Removido com sucesso.")

                    hotel_existe = True

                    break

            if not hotel_existe:
                raise Exception(
                    f"Hotel de código [{codigo}] não foi encontrada para ser removida."
                )
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def listar(self):
        try:
            if not len(self.__hoteis) >= 1:
                raise ListaVaziaException('hoteis')
            lista_dados_hotel = list(map(
                lambda hotel: {
                    "nome": hotel.nome,
                    "endereco": hotel.endereco,
                    "codigo": hotel.codigo,
                    "telefone": hotel.telefone
                }, self.__hoteis))

            self.__tela_hotel.mostrar_hoteis(lista_dados_hotel)
            return True
        except ListaVaziaException as e:
            self.__tela_hotel.mostra_mensagem(str(e))
            return False

    def alterar(self):
        if not self.listar():
            return

        dados_hotel = self.__tela_hotel.pega_dados_hotel()
        
        try:
            hotel_existe = False
            for hotel in self.__hoteis:
                if hotel.codigo == dados_hotel["codigo"]:
                    hotel.nome = dados_hotel["nome"]
                    hotel.endereco = dados_hotel["endereco"]
                    hotel.telefone = dados_hotel["telefone"]

                    self.__tela_hotel.mostra_mensagem("Alterado com sucesso.")

                    hotel_existe = True

                    break

            if not hotel_existe:
                raise Exception(
                    f"Hotel de código [{dados_hotel['codigo']}] não foi encontrada."
                )
        except Exception as e:
            self.__tela_hotel.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        for hotel in self.__hoteis:
            if hotel.codigo == codigo:
                return hotel

        return None

    def relatorio_geral(self):
        try:
            lista_dados_hoteis = []
            for hotel in self.__hoteis:
                lista_reservas = self.__controlador_sistema.controlador_reserva.listar_reservas_por_hotel(
                    hotel.codigo)

                lista_dados_hoteis.append({
                    "nome": hotel.nome,
                    "codigo": hotel.codigo,
                    "numero_funcionarios": len(hotel.funcionarios),
                    "numero_clientes": len(hotel.clientes),
                    "numero_quartos": hotel.numero_de_quartos(),
                    "numero_reservas": len(lista_reservas),
                    "faturamento_total_em_reservas": sum(reserva.custo for reserva in lista_reservas)
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
