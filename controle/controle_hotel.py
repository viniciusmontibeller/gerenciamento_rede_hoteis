from limite.tela_hotel import TelaHotel
from entidade.hotel import Hotel


class ControladorHotel():

    def __init__(self, controlador_sistema):
        self.__hoteis = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_hotel = TelaHotel()

    def adicionar(self):
        dados_hotel = self.__tela_hotel.pega_dados_hotel()
        if self.buscar_por_codigo(dados_hotel["codigo"]):
            raise Exception("Hotel ja existente")
        else:
            self.__hoteis.append(
                Hotel(dados_hotel["nome"], dados_hotel["codigo"],
                      dados_hotel["endereco"], dados_hotel["telefone"]))

    def remover(self):
        codigo = self.__tela_hotel.pega_codigo_hotel()
        hotel_existe = False

        for hotel in self.__hoteis:
            if hotel.codigo == codigo:
                self.__hoteis.remove(hotel)
                self.__tela_hotel.mosta_mensagem("Removido com sucesso.")

                hotel_existe = True

                break

        if not hotel_existe:
            raise Exception(
                f"Hotel de código [{codigo}] não foi encontrada para ser removida."
            )

    def listar(self):
        return map(
            lambda hotel: {
                "nome": hotel.nome,
                "endereço": hotel.endereco,
                "codigo": hotel.codigo
            }, self.__hoteis)

    def alterar(self):
        self.__tela_hotel.mostra_hotel(self.listar())

        dados_hotel = self.__tela_hotel.pega_dados_hotel()
        hotel_existe = False

        for hotel in self.__hoteis:
            if hotel.codigo == dados_hotel["codigo"]:
                self.__hoteis[hotel.codigo]["nome"] = dados_hotel["nome"]
                self.__hoteis[hotel.codigo]["localizacao_hotel"] = dados_hotel[
                    "localizacao_hotel"]

                self.__tela_hotel.mosta_mensagem("Alterado com sucesso.")

                hotel_existe = True

                break

        if not hotel_existe:
            raise Exception(
                f"Hotel de código [{dados_hotel['codigo']}] não foi encontrada."
            )

    def buscar_por_codigo(self, codigo):
        for hotel in self.__hoteis:
            if hotel.codigo == codigo:
                return hotel

        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_hotel.tela_opcoes()]()
