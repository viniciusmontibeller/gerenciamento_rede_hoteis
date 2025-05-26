from limite.abstract_tela import AbstractTela

class TelaHotel(AbstractTela):

    def tela_opcoes(self):
        print("\n")
        print("-------- Hoteis --------")
        print("Selecione a opção desejada")
        print("1 - Gerenciar Funcionários de um Hotel")
        print("2 - Gerenciar Clientes de um Hotel")
        print("3 - Gerenciar Quartos de um Hotel")
        print("4 - Incluir Hotel")
        print("5 - Alterar Hotel")
        print("6 - Listar Hoteis")
        print("7 - Excluir Hoteis")
        print("8 - Relatório Geral de Hoteis")
        print("0 - Retornar")
        print("\n")

        opcao = super().le_input_int_com_range_de_validacao("Opção escohida: ", [0, 1, 2, 3, 4, 5, 6, 7, 8])
        return opcao

    def pega_dados_hotel(self):
        print("\n")
        print("-------- Dados do Hotel --------")
        dados_hotel = {}
        dados_hotel["nome"] = input("Nome: ")
        dados_hotel["codigo"] = super().le_input_so_int("Codigo: ")
        dados_hotel["endereco"] = input("Endereço: ")
        dados_hotel["telefone"] = super().le_input_so_int("Telefone: ")

        return dados_hotel

    def mostrar_hoteis(self, lista_dados_hotel):
        print("\n")
        print("-------- Listagem de Hoteis --------")
        for dados_hotel in lista_dados_hotel:
            self.mostra_hotel(dados_hotel)

    def mostra_hotel(self, dados_hotel):
        print("\n")
        print("Nome do hotel: ", dados_hotel["nome"])
        print("Código do hotel: ", dados_hotel["codigo"])
        print("Endereço do hotel: ", dados_hotel["endereco"])
        print("Telefone do hotel: ", dados_hotel["telefone"])
        print("\n")

    def pega_codigo_hotel(self):
        return super().le_input_so_int("Código do hotel: ")

    def mostra_relatorio(self, lista_dados_hoteis):
        print("\n")
        print("-------- Relatório Geral de Hoteis --------")
        print("\n")

        for dados_hotel in lista_dados_hoteis:
            print("Nome do hotel: ", dados_hotel["nome"])
            print("Código do hotel: ", dados_hotel["codigo"])
            print("Funcionários do hotel: ", dados_hotel["numero_funcionarios"])
            print("Clientes do hotel: ", dados_hotel["numero_clientes"])
            print("Quartos do hotel: ", dados_hotel["numero_quartos"])
            print("Número de reservas: ", dados_hotel["numero_reservas"])
            print("Faturamento total em reservas: ", dados_hotel["faturamento_total_em_reservas"])
            print("\n")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
