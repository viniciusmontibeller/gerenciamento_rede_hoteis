from limite.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  

    def tela_opcoes(self):
        print("\n")
        print("-------- Cliente --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Remover Cliente")
        print("0 - Retornar")
        print("\n")

        opcao = super().le_input_int("Opção escolhida: ", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_cliente(self):
        print("-------- Dados do Cliente --------")
        dados_cliente = {}
        dados_cliente["nome"] = input("Nome: ")
        dados_cliente["cpf"] = super().le_input_so_numero("CPF: ")
        dados_cliente["telefone"] = super(
        ).le_input_so_numero("Telefone: ")
        dados_cliente["email"] = input("Email: ")

        return dados_cliente

    def mostrar_clientes(self, lista_dados_cliente):
        print("\n")
        print("-------- Listagem de Clientes --------")
        for dados_cliente in lista_dados_cliente:
            self.mostra_cliente(dados_cliente)

    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("Código do cliente: ", dados_cliente["cpf"])
        print("Telefone do cliente: ", dados_cliente["telefone"])
        print("Email do cliente: ", dados_cliente["email"])
        print("\n")

    def pega_cpf_cliente(self):
        return super().le_input_so_numero("CPF do cliente: ")

    def pega_codigo_hotel(self):
        return super().le_input_so_numero("Código do hotel: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)