from abstract_tela import AbstractTela

class TelaFuncionario(AbstractTela):
    
    def tela_opcoes(self):
        print("-------- Funcionario --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Funcionario")
        print("2 - Alterar Funcionario")
        print("3 - Listar Funcionarios")
        print("4 - Buscar Funcionario")
        print("5 - Excluir Funcionario")
        print("0 - Retornar")
        opcao = super().le_input_int("Opção escohida: ")
        return opcao
    
    def pega_dados_funcionario(self):
        print("-------- Dados do Funcionario --------")
        dados_funcionario = {}
        dados_funcionario["nome"] = str(input("Nome: "))
        dados_funcionario["cpf"] = str(input("Cpf: "))
        dados_funcionario["telefone"] = str(input("Telefone: "))
        dados_funcionario["email"] = str(input("Email: "))

        return dados_funcionario
    
    def mostra_funcionario(self, dados_funcionario):
        print("Nome do funcionario: ", dados_funcionario["nome"])
        print("Código do funcionario: ", dados_funcionario["codigo"])
        print("Telefone do funcionario: ", dados_funcionario["telefone"])
        print("Email do funcionario: ", dados_funcionario["email"])
        print("\n")
    
    def pega_cpf_funcionario(self):
        return input("Código do funcionario: ")
    
    def mosta_mensagem(self, mensagem):
        print(mensagem)