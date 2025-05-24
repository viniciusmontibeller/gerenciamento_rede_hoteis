from limite.tela_rede import TelaRede
from entidade.rede import Rede


class ControladorRede():

    def __init__(self, controlador_sistema):
        self.__redes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_rede = TelaRede()

    def adicionar(self):
        dados_rede = self.__tela_rede.pega_dados_rede()
        if self.buscar_por_codigo(dados_rede["codigo"]):
            raise Exception("Rede ja existente")
        else:
            self.__redes.append(
                Rede(dados_rede["nome"], dados_rede["codigo"],
                     dados_rede["localizacao_rede"]))

    def remover(self):
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

    def buscar_por_codigo(self, codigo):
        for rede in self.__redes:
            if rede.codigo == codigo:
                return rede

        return None

    def listar(self):
        return map(
            lambda rede: {
                "nome": rede.nome,
                "localizacao_rede": rede.localizacao_rede,
                "codigo": rede.codigo
            }, self.__redes)

    def alterar(self):
        self.__tela_rede.mostrar_redes(self.listar())

        dados_rede = self.__tela_rede.pega_dados_rede_para_alteracao()
        rede_existe = False

        for rede in self.__redes:
            if rede.codigo == dados_rede["codigo"]:
                self.__redes[rede.codigo]["nome"] = dados_rede["nome"]
                self.__redes[rede.codigo]["localizacao_rede"] = dados_rede[
                    "localizacao_rede"]

                self.__tela_rede.mostra_mensagem("Alterado com sucesso.")

                rede_existe = True

                break

        if not rede_existe:
            raise Exception(
                f"Rede de código [{dados_rede['codigo']}] não foi encontrada.")

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_rede.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
