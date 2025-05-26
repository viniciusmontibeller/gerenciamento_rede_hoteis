from limite.tela_rede import TelaRede
from entidade.rede import Rede


class ControladorRede():

    def __init__(self, controlador_sistema):
        self.__redes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_rede = TelaRede()

    def adicionar(self):
        dados_rede = self.__tela_rede.pega_dados_rede()
        try:
            if self.buscar_por_codigo(dados_rede["codigo"]):
                raise Exception("Rede ja existente")
            self.__redes.append(
                Rede(dados_rede["nome"], dados_rede["codigo"],
                        dados_rede["localizacao_rede"]))
            self.__tela_rede.mostra_mensagem("Rede adicionada com sucesso!")
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def remover(self):
        self.listar()
        try:
            if not len(self.__redes) >= 1:
                raise Exception("Não existe nenhuma rede para ser alterada")
            codigo = self.__tela_rede.pega_codigo_rede()
            rede_existe = False

            for rede in self.__redes:
                if rede.codigo == codigo:
                    self.__redes.remove(rede)
                    self.__tela_rede.mostra_mensagem("Removido com sucesso.")

                    rede_existe = True

                    break

            if not rede_existe:
                raise Exception(
                    f"Rede de código [{codigo}] não foi encontrada para ser removida."
                )
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        for rede in self.__redes:
            if rede.codigo == codigo:
                return rede

        return None

    def listar(self):
        lista_dados_rede = map(
            lambda rede: {
                "nome": rede.nome,
                "localizacao_rede": rede.localizacao_rede,
                "codigo": rede.codigo,
                "hoteis": rede.hoteis
            }, self.__redes)

        self.__tela_rede.mostrar_redes(lista_dados_rede)

    def alterar(self):
        self.listar()
        
        try:
            if not len(self.__redes) >= 1:
                raise Exception("Não existe nenhuma rede para ser removida")
            dados_rede = self.__tela_rede.pega_dados_rede_para_alteracao()
            rede_existe = False
            for rede in self.__redes:
                if rede.codigo == dados_rede["codigo"]:
                    rede.nome = dados_rede["nome"]
                    rede.localizacao_rede = dados_rede["localizacao_rede"]

                    self.__tela_rede.mostra_mensagem("Alterado com sucesso.")

                    rede_existe = True

                    break

            if not rede_existe:
                raise Exception(
                    f"Rede de código [{dados_rede['codigo']}] não foi encontrada.")
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))


    def adicionar_hotel_em_rede(self):
        dados_inclusao = self.__tela_rede.pega_dados_inclusao_de_hotel()

        rede = self.buscar_por_codigo(dados_inclusao["codigo_rede"])
        hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_inclusao["codigo_hotel"])
        try:
            if not rede:
                raise Exception("Rede não encontrada")
            if not hotel:
                raise Exception("Hotel não encontrado")

            rede.adicionar_hotel(hotel)
            self.__tela_rede.mostra_mensagem("Hotel adicionado com sucesso.")
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            5: self.adicionar_hotel_em_rede,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_rede.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
