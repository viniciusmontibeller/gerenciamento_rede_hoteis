from controle.controle_cliente import ControladorCliente
from controle.controle_funcionario import ControladorFuncionario
from limite.tela_hotel import TelaHotel
from entidade.hotel import Hotel


class ControladorHotel():

    def __init__(self, controlador_sistema):
        self.__hoteis = []
        self.__controlador_sistema = controlador_sistema
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__tela_hotel = TelaHotel()

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
        lista_dados_hotel = list(map(
            lambda hotel: {
                "nome": hotel.nome,
                "endereco": hotel.endereco,
                "codigo": hotel.codigo,
                "telefone": hotel.telefone
            }, self.__hoteis))
        
        self.__tela_hotel.mostrar_hoteis(lista_dados_hotel)

    def alterar(self):
        self.listar()

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

    def gerenciar_funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def gerenciar_clientes(self):
        self.__controlador_cliente.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.gerenciar_funcionarios,
            2: self.gerenciar_clientes,
            3: self.adicionar,
            4: self.alterar,
            5: self.listar,
            6: self.remover,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_hotel.tela_opcoes()]()
