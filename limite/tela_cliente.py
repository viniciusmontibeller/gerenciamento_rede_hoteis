from abstract_tela import AbstractTela

class TelaCliente(AbstractTela):

    def tela_opcoes(self):
        print("-------- Cliente --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Buscar Cliente")
        print("5 - Excluir Cliente")
        print("0 - Retornar")
        opcao = super().le_input_int("Opção escohida", [0,1,2,3,4,5])
        return opcao

    def pega_dados_cliente(self):
        print("-------- Dados do Cliente --------")
        dados_cliente = {}
        dados_cliente["nome"] = input("Nome: ")
        dados_cliente["cpf"] = super.le_input_so_numero("CPF: ")
        dados_cliente["telefone"] = super().le_input_so_numero("Telefone: ")
        dados_cliente["email"] = input("Email: ")

        return dados_cliente

    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF do cliente: ", dados_cliente["cpf"])
        print("Telefone do cliente: ", dados_cliente["telefone"])
        print("Email do cliente: ", dados_cliente["email"])
        print("\n")

    def pega_cpf_cliente(self):
        return super().le_input_so_numero("CPF do cliente: ")

    def mosta_mensagem(self, mensagem):
        print(mensagem)
