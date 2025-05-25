from limite.abstract_tela import AbstractTela

class TelaHotel(AbstractTela):

    def tela_opcoes(self):
        print("\n")
        print("-------- Hoteis --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Hotel")
        print("2 - Alterar Hotel")
        print("3 - Listar Hoteis")
        print("4 - Excluir Hoteis")
        print("0 - Retornar")
        
        opcao = super().le_input_int("Opção escohida: ", [0,1,2,3,4])
        return opcao

    def pega_dados_hotel(self):
        print("-------- Dados do Hotel --------")
        dados_hotel = {}
        dados_hotel["nome"] = input("Nome: ")
        dados_hotel["codigo"] = super().le_input_so_numero("Codigo: ")
        dados_hotel["localizacao"] = input("Endereço: ")
        dados_hotel["telefone"] = super().le_input_so_numero("Telefone: ")

        return dados_hotel

    def mostra_hotel(self, dados_hotel):
        print("Nome do hotel: ", dados_hotel["nome"])
        print("Código do hotel: ", dados_hotel["codigo"])
        print("Endereço do hotel: ", dados_hotel["endereco"])
        print("Telefone do hotel: ", dados_hotel["telefone"])
        print("\n")

    def pega_codigo_hotel(self):
        return super().le_input_so_numero("Código do hotel: ")

    def mosta_mensagem(self, mensagem):
        print(mensagem)
