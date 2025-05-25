from limite.abstract_tela import AbstractTela

class TelaReserva(AbstractTela):

    def pega_dados_reserva(self):
        dados_reserva = {}
        dados_reserva["codigo"] = str(input("Codigo da reserva: "))
        dados_reserva["cpf_cliente"] = str(input("CPF do cliente: "))
        dados_reserva["codigo_hotel"] = str(input("Codigo do hotel: "))
        dados_reserva["codigo_quarto"] = str(input("Codigo do quarto: "))
        dados_reserva["codigo_funcionario"] = str(input("Codigo do funcionario: "))
        dados_reserva["data_entrada"] = super().le_input_data("Data de entrada (DD-MM-YYYY): ")
        dados_reserva["data_saida"] = super().le_input_data("Data de saida (DD-MM-YYYY): ")

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
        return super().le_input_so_numero("Codigo da reserva: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def tela_opcoes(self):
        print("\n")
        print("-------- RESERVAS ----------")
        print("Selecione a opção desejada")
        print("1 - Adicionar reserva")
        print("2 - Alterar reserva")
        print("3 - Listar reserva")
        print("4 - Remover reserva")
        print("0 - Retornar")
        print("\n")

        opcao = super().le_input_int("Escolha a opcao: ", [0, 1, 2, 3, 4])
        return opcao
