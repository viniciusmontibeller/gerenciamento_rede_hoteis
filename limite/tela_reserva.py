from limite.abstract_tela import AbstractTela
from excecoes.data_saida_invalida_exception import DataSaidaInvalidaException

class TelaReserva(AbstractTela):

    def pega_dados_reserva(self):
        print("\n")
        print("-------- Dados da Reserva --------")
        dados_reserva = {}
        dados_reserva["codigo_hotel"] = super().le_input_so_int("Codigo do hotel: ")
        dados_reserva["codigo_quarto"] = super().le_input_so_int("Número do quarto: ")
        dados_reserva["cpf_cliente"] = super().le_input_so_numero("CPF do cliente: ")
        dados_reserva["cpf_funcionario"] = super().le_input_so_numero("CPF do funcionario: ")
        dados_reserva["data_entrada"] = super().le_input_data("Data de entrada (DD-MM-YYYY): ")
        while True:
            valor_lido = super().le_input_data("Data de saida (DD-MM-YYYY): ")
            try:
                if dados_reserva["data_entrada"] > valor_lido:
                    raise DataSaidaInvalidaException(dados_reserva["data_entrada"])
                dados_reserva["data_saida"] = valor_lido
                break
            except DataSaidaInvalidaException as e:
                print(e)

        return dados_reserva

    def mostrar_reservas(self, lista_dados_reserva):
        print("\n")
        print("-------- Listagem de Reservas --------")
        print("\n")
        
        for dados_reserva in lista_dados_reserva:
            self.mostrar_reserva(dados_reserva)

    def mostrar_reserva(self, dados_reserva):
        print("\n")
        print(f"Codigo da reserva: {dados_reserva['codigo']}")
        print(f"Cliente da reserva: {dados_reserva['cliente']}")
        print(f"Hotel da reserva: {dados_reserva['hotel']}")
        print(f"Quarto da reserva: {dados_reserva['quarto']}")
        print(f"Funcionario responsável: {dados_reserva['funcionario']}")
        print(f"Data de entrada: {dados_reserva['data_entrada']}")
        print(f"Data de saída: {dados_reserva['data_saida']}")
        print(f"Status da reserva: {dados_reserva['status']}")
        print(f"Custo da reserva: R${dados_reserva['custo']}")
        print("\n")

    def pega_codigo_reserva(self):
        return super().le_input_so_int("Codigo da reserva: ")

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

        opcao = super().le_input_int_com_range_de_validacao("Escolha a opcao: ", [0, 1, 2, 3, 4])
        return opcao
