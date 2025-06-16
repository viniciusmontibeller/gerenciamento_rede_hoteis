from limite.abstract_tela import AbstractTela


class TelaFuncionario(AbstractTela):

    def tela_opcoes(self):
        print("\n")
        print("-------- Funcionario --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Funcionario")
        print("2 - Alterar Funcionario")
        print("3 - Listar Funcionarios")
        print("4 - Remover Funcionario")
        print("0 - Retornar")
        print("\n")

        opcao = super().le_input_int_com_range_de_validacao("Opção escolhida: ", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_funcionario(self):
        print("\n")
        print("-------- Dados do Funcionario --------")
        dados_funcionario = {}
        dados_funcionario["nome"] = input("Nome: ")
        dados_funcionario["cpf"] = super().le_cpf("CPF: ")
        dados_funcionario["telefone"] = super(
        ).le_telefone("Telefone: ")
        dados_funcionario["email"] = input("Email: ")

        return dados_funcionario

    def mostrar_funcionarios(self, lista_dados_funcionario):
        print("\n")
        print("-------- Listagem de Funcionarios --------")
        print("\n")
        for dados_funcionario in lista_dados_funcionario:
            self.mostra_funcionario(dados_funcionario)

    def mostra_funcionario(self, dados_funcionario):
        print("\n")
        print("Nome do funcionario: ", dados_funcionario["nome"])
        print("CPF do funcionario: ", dados_funcionario["cpf"])
        print("Telefone do funcionario: ", dados_funcionario["telefone"])
        print("Email do funcionario: ", dados_funcionario["email"])
        print("\n")

    def pega_cpf_funcionario(self):
        return super().le_cpf("CPF do funcionario: ")

    def pega_codigo_hotel(self):
        return super().le_input_so_int("Código do hotel: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
