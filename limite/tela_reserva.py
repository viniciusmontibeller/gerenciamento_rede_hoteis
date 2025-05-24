from abstract_tela import AbstractTela

class TelaReserva(AbstractTela):

    def pega_dados_reserva(self):
        dados_reserva = {}
        dados_reserva["codigo"] = str(input("Codigo: "))
        dados_reserva["nome_cliente"] = str(input("Nome do cliente: "))
        dados_reserva["cpf_cliente"] = str(input("Cpf do cliente: "))
        dados_reserva["telefone_cliente"] = str(input("Telefone do cliente: "))
        dados_reserva["email_cliente"] = str(input("Email cliente: "))
        dados_reserva["numero_quarto"] = int(input("Numero do quarto: "))
        dados_reserva["capacidade_quarto"] = int(
            input("Capacidade do quarto: "))
        dados_reserva["preco_diaria_quarto"] = float(
            input("Preco diaria do quarto: "))
        dados_reserva["nome_funcionario"] = str(input("Nome do funcionario: "))
        dados_reserva["cpf_funcionario"] = str(input("Cpf do funcionario: "))
        dados_reserva["telefone_funcionario"] = str(
            input("Telefone do funcionario: "))
        dados_reserva["email_funcionario"] = str(
            input("Email do funcionario: "))

        return dados_reserva

    def mostrar_reservas(self, lista_dados_reserva):
        for dados_reserva in lista_dados_reserva:
            self.mostrar_reserva(dados_reserva)

    def mostrar_reserva(self, dados_reserva):
        print(f"Codigo da reserva: {dados_reserva['codigo']}")
        print(f"Cliente da reserva: {dados_reserva['cliente']}")
        print(f"Quarto da reserva: {dados_reserva['quarto']}")
        print(f"Funcionario responsável: {dados_reserva['funcionario']}")

    def pega_codigo_reserva(self):
        return input("Codigo da reserva: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def tela_opcoes(self):
        print("-------- RESERVAS ----------")
        print("Escolha a opcao")
        print("1 - Adicionar reserva")
        print("2 - Alterar reserva")
        print("3 - Remover reserva")
        print("4 - Listar reserva")
        print("0 - Retornar")

        opcao = super().le_input_int("Escolha a opcao: ")
        return opcao
