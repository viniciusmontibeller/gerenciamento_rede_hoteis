class TelaRede:

    def pega_dados_rede(self):
        dados_rede = {}
        dados_rede["nome"] = str(input("Nome: "))
        dados_rede["codigo"] = str(input("Codigo: "))
        dados_rede["localizacao_rede"] = str(input("Localizacao: "))

        return dados_rede

    def pega_dados_rede_para_alteracao(self):
        dados_rede = {}
        dados_rede["codigo"] = str(input("Codigo da rede que será alterada: "))
        dados_rede["nome"] = str(input("Novo nome: "))
        dados_rede["localizacao_rede"] = str(input("Nova localização: "))

        return dados_rede

    def mostrar_redes(self, lista_dados_rede):
        for dados_rede in lista_dados_rede:
            self.mostrar_rede(dados_rede)

    def mostrar_rede(self, dados_rede):
        print(f"Nome da rede: {dados_rede['nome']}")
        print(f"Codigo da rede: {dados_rede['codigo']}")
        print(f"Localização da rede: {dados_rede['localizacao_rede']}")

    def pega_codigo_rede(self):
        return input("Codigo da rede: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def tela_opcoes(self):
        print("-------- REDES ----------")
        print("Escolha a opcao")
        print("1 - Adiicionar Rede")
        print("2 - Alterar Rede")
        print("3 - Remover Rede")
        print("4 - Listar Rede")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
