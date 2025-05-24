from abstract_tela import AbstractTela

class TelaHotel(AbstractTela):
    
    def le_input_so_float(self, mensagem):
        while True:
            valor_lido = input(mensagem)
            try:
                if not isinstance(valor_lido, float):
                    raise ValueError
                return float(valor_lido)
            except ValueError:
                print("Valor incorreto! Somente valores em dinheiro")
    
    def tela_opcoes(self):
        print("-------- Quartos --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Quarto")
        print("2 - Alterar Quarto")
        print("3 - Listar Quartos")
        print("4 - Buscar Quarto")
        print("5 - Excluir Quartos")
        print("0 - Retornar")
        opcao = super().le_input_int("Opção escohida", [0,1,2,3,4,5])
        return opcao
    
    def pega_dados_quarto(self):
        print("-------- Dados do quarto --------")
        dados_quarto = {}
        dados_quarto["numero"] = input("NUmero: ")
        dados_quarto["capacidade"] = super().le_input_so_numero("Capacidade: ")
        dados_quarto["preco_diaria"] = self.le_input_so_float("Preço da diaria: ")
    
    def mostra_quarto(self, dados_quarto):
        print("Numero do quarto: ", dados_quarto["numero"])
        print("Capacidade do quarto: ", dados_quarto["capacidade"])
        print("Precço diaria do quarto: ", dados_quarto["preco_diaria"])
        print("\n")
    
    def pega_codigo_quarto(self):
        return super().le_input_so_numero("Código do quarto: ")
    
    def mosta_mensagem(self, mensagem):
        print(mensagem)