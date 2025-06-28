from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaHotel(AbstractTela):

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Gerenciar Funcionários de um Hotel': 1,
            'Gerenciar Clientes de um Hotel': 2,
            'Gerenciar Quartos de um Hotel': 3,
            'Incluir Hotel': 4,
            'Alterar Hotel': 5,
            'Listar Hoteis': 6,
            'Excluir Hoteis': 7,
            'Relatório Geral de Hoteis': 8,
            'Retornar': 0,
            None: 0,
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[
            sg.Text('Bem vindo ao sistema de gerenciamento de redes e hotéis',
                    font=("Helvetica", 25))
        ], [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
                  [sg.Button('Gerenciar Funcionários de um Hotel')],
                  [sg.Button('Gerenciar Clientes de um Hotel')],
                  [sg.Button('Gerenciar Quartos de um Hotel')],
                  [sg.Button('Incluir Hotel')], [sg.Button('Alterar Hotel')],
                  [sg.Button('Listar Hoteis')], [sg.Button('Excluir Hoteis')],
                  [sg.Button('Relatório Geral de Hoteis')],
                  [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_hotel(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[
            sg.Text('DADOS HOTEL',
                    font=("Helvica", 20),
                    justification="center")
        ],
                  [
                      sg.Text('Nome:', size=(15, 1)),
                      sg.InputText(key='nome', tooltip='Nome da rede')
                  ],
                  [
                      sg.Text('Código:', size=(15, 1)),
                      sg.InputText(key='codigo',
                                   tooltip='Apenas números (ex: 123)')
                  ],
                  [
                      sg.Text('Endereço:', size=(15, 1)),
                      sg.InputText(key='endereco',
                                   tooltip='Informe o endereço')
                  ],
                  [
                      sg.Text('Telefone:', size=(15, 1)),
                      sg.InputText(key='telefone',
                                   tooltip='Informe o telefone')
                  ], [sg.Button('Confirmar'),
                      sg.Cancel('Cancelar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = self.__window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None

            if not self._validar_campos(
                    values, [("obrigatorio", "nome", "Nome"),
                             ("numero", "codigo", "Código"),
                             ("obrigatorio", "endereco", "Endereço"),
                             ("obrigatorio", "telefone", "Telefone")]):
                continue

            dados_rede = {
                "nome": self._extrair_valor(values, 'nome'),
                "codigo": int(self._extrair_valor(values, 'codigo')),
                "endereco": self._extrair_valor(values, 'endereco'),
                "telefone": self._extrair_valor(values, 'telefone')
            }

            self.close()
            return dados_rede

    def mostrar_hoteis(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- LISTA DE HOTEIS ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "Nome do hotel: " + str(dados["nome"]) + "\n"
        string_dados += "Código do hotel: " + str(dados["codigo"]) + "\n"
        string_dados += "Endereço do hotel: " + str(dados["endereco"]) + "\n"
        string_dados += "Telefone do hotel: " + str(dados["telefone"]) + "\n"
        string_dados += '\n'

        return string_dados

    def mostra_relatorio(self, lista_dados_hoteis):
        print("\n")
        print("-------- Relatório Geral de Hoteis --------")
        print("\n")

        for dados_hotel in lista_dados_hoteis:
            print("Nome do hotel: ", dados_hotel["nome"])
            print("Código do hotel: ", dados_hotel["codigo"])
            print("Funcionários do hotel: ",
                  dados_hotel["numero_funcionarios"])
            print("Clientes do hotel: ", dados_hotel["numero_clientes"])
            print("Quartos do hotel: ", dados_hotel["numero_quartos"])
            print("Número de reservas: ", dados_hotel["numero_reservas"])
            print("Faturamento total em reservas: ",
                  dados_hotel["faturamento_total_em_reservas"])
            print("\n")

    def close(self):
        self.__window.Close()
