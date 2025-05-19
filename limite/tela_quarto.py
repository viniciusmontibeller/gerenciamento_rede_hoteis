class TelaHotel():
    
    def tela_opcoes(self):
        print("-------- Quartos --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Quarto")
        print("2 - Alterar Quarto")
        print("3 - Listar Quartos")
        print("4 - Buscar Quarto")
        print("5 - Excluir Quartos")
        print("0 - Retornar")
        opcao = int(input("Opção escohida"))  # Falta adicionar verificação de input de usuario
        return opcao
    
    def pega_dados_quarto(self):
        print("-------- Dados do quarto --------")
        dados_quarto = {}
        dados_quarto["numero"] = str(input("NUmero: "))
        dados_quarto["capacidade"] = str(input("Capacidade: "))
        dados_quarto["preco_diario"] = str(input("Preco diaria: "))

        return dados_quarto
    
    def mostra_quarto(self, dados_quarto):
        print("Numero do quarto: ", dados_quarto["numero"])
        print("Capacidade do quarto: ", dados_quarto["capacidade"])
        print("Precço diaria do quarto: ", dados_quarto["preco_diaria"])
        print("\n")
    
    def pega_codigo_quarto(self):
        return input("Código do quarto: ")
    
    def mosta_mensagem(self, mensagem):
        print(mensagem)