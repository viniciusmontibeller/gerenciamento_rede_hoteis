class TelaCliente():
    
    def tela_opcoes(self):
        print("-------- Cliente --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Buscar Cliente")
        print("5 - Excluir Cliente")
        print("0 - Retornar")
        opcao = int(input("Opção escohida"))  # Falta adicionar verificação de input de usuario
        return opcao
    
    def pega_dados_cliente(self):
        print("-------- Dados do Cliente --------")
        dados_cliente = {}
        dados_cliente["nome"] = str(input("Nome: "))
        dados_cliente["codigo"] = str(input("Codigo: "))
        dados_cliente["telefone"] = str(input("Telefone: "))
        dados_cliente["email"] = str(input("Email: "))

        return dados_cliente
    
    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("Código do cliente: ", dados_cliente["codigo"])
        print("Telefone do cliente: ", dados_cliente["telefone"])
        print("Email do cliente: ", dados_cliente["email"])
        print("\n")
    
    def pega_codigo_cliente(self):
        return input("Código do cliente: ")
    
    def mosta_mensagem(self, mensagem):
        print(mensagem)