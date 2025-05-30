from limite.abstract_tela import AbstractTela

class TelaRede(AbstractTela):

    def pega_dados_rede(self):
        dados_rede = {}
        dados_rede["nome"] = input("Nome: ")
        dados_rede["codigo"] = super().le_input_so_int("Codigo: ")
        dados_rede["localizacao_rede"] = input("Localizacao: ")

        return dados_rede

    def pega_dados_rede_para_alteracao(self):
        dados_rede = {}
        dados_rede["codigo"] = super().le_input_so_int("Codigo da rede que será alterada: ")
        dados_rede["nome"] = input("Novo nome: ")
        dados_rede["localizacao_rede"] = input("Nova localização: ")

        return dados_rede

    def pega_dados_inclusao_de_hotel(self):
        dados_inclusao = {}
        dados_inclusao["codigo_rede"] = super().le_input_so_int("Código da rede: ")
        dados_inclusao["codigo_hotel"] = super().le_input_so_int("Código do hotel que será adicionado na rede: ")

        return dados_inclusao


    def mostrar_redes(self, lista_dados_rede):
        for dados_rede in lista_dados_rede:
            self.mostrar_rede(dados_rede)

    def mostrar_rede(self, dados_rede):
        print("\n")
        print(f"Nome da rede: {dados_rede['nome']}")
        print(f"Codigo da rede: {dados_rede['codigo']}")
        print(f"Localização da rede: {dados_rede['localizacao_rede']}")
        print(f"Hoteis da rede: {', '.join([str(hotel.codigo) for hotel in dados_rede['hoteis']])}")
        print("\n")

    def pega_codigo_rede(self):
        return super().le_input_so_int("Codigo da rede: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def tela_opcoes(self):
        print("\n")
        print("-------- REDES ----------")
        print("Selecione a opção desejada")
        print("1 - Adicionar Rede")
        print("2 - Alterar Rede")
        print("3 - Listar Rede")
        print("4 - Remover Rede")
        print("5 - Adicionar Hotel em Rede")
        print("0 - Retornar")
        print("\n")

        opcao = super().le_input_int_com_range_de_validacao("Escolha a opcao: ", [0,1,2,3,4,5])
        return opcao
