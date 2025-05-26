from limite.abstract_tela import AbstractTela


class TelaQuarto(AbstractTela):

    def __le_input_eh_quarto_vip_bool(self, mensagem: str) -> bool:
        while True:
            entrada = input(mensagem)
            entrada = entrada.strip().lower()
            try:
                if entrada in ['sim', 's']:
                    return True
                elif entrada in ['não', 'nao', 'n']:
                    return False
                else:
                    raise ValueError
            except ValueError:
                print("Entrada inválida para fidelidade. Use sim/s ou não/n.")


    def tela_opcoes(self):
        print("\n")
        print("-------- Quartos --------")
        print("Selecione a opção desejada")
        print("1 - Incluir Quarto")
        print("2 - Alterar Quarto")
        print("3 - Listar Quartos")
        print("4 - Excluir Quartos")
        print("0 - Retornar")
        print("\n")
        
        opcao = super().le_input_int_com_range_de_validacao("Opção escolhida: ", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_quarto(self):
        print("\n")
        print("-------- Dados do quarto --------")
        dados_quarto = {}
        dados_quarto["numero"] = super().le_input_so_int("Número: ")
        dados_quarto["capacidade"] = super().le_input_so_int("Capacidade: ")
        dados_quarto["preco_diaria"] = super().le_input_so_float("Preço da diaria: ")
        
        return dados_quarto

    def pega_eh_quarto_vip(self):
        return self.__le_input_eh_quarto_vip_bool("É quarto vip? (s/n): ")

    def mostrar_quartos(self, lista_dados_quarto):
        print("\n")
        print("-------- Listagem de Quartos --------")
        print("\n")
        for dados_quarto in lista_dados_quarto:
            self.mostra_quarto(dados_quarto)

    def mostra_quarto(self, dados_quarto):
        print("\n")
        print("Numero do quarto: ", dados_quarto["numero"])
        print("Capacidade do quarto: ", dados_quarto["capacidade"])
        print("Preço da diaria do quarto: ", dados_quarto["preco_diaria"])
        print("\n")

    def pega_codigo_hotel(self):
        return super().le_input_so_int("Código do hotel: ")

    def pega_numero_quarto(self):
        return super().le_input_so_int("Número do quarto: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

