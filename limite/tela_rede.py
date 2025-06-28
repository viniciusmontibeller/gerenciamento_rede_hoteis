from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaRede(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def pega_dados_rede(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[
            sg.Text('DADOS REDE', font=("Helvica", 20), justification="center")
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
                      sg.Text('Localização da rede:', size=(15, 1)),
                      sg.InputText(key='localizacao',
                                   tooltip='Informe a cidade')
                  ], [sg.Button('Confirmar'),
                      sg.Cancel('Cancelar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = self.__window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None

            if not self._validar_campos(values, [
                ("obrigatorio", "nome", "Nome"),
                ("numero", "codigo", "Código"),
                ("obrigatorio", "localizacao", "Localização da rede")
            ]):
                continue

            dados_rede = {
                "nome": self._extrair_valor(values, 'nome'),
                "codigo": int(self._extrair_valor(values, 'codigo')),
                "localizacao_rede": self._extrair_valor(values, 'localizacao')
            }

            self.close()
            return dados_rede

    def pega_dados_inclusao_de_hotel(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[
            sg.Text('DADOS HOTEL',
                    font=("Helvica", 20),
                    justification='center')
        ],
                  [
                      sg.Text('Código da Rede:', size=(15, 1)),
                      sg.InputText(key='codigo_rede',
                                   tooltip='Apenas números (ex: 123)')
                  ],
                  [
                      sg.Text('Código do Hotel:', size=(15, 1)),
                      sg.InputText(key='codigo_hotel',
                                   tooltip='Apenas números (ex: 123)')
                  ], [sg.Button('Confirmar'),
                      sg.Cancel('Cancelar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = self.__window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None

            if not self._validar_campos(values, [
                ("obrigatorio", "codigo_rede", "Código da Rede"),
                ("numero", "codigo_rede", "Código da Rede"),
                ("obrigatorio", "codigo_hotel", "Código do Hotel"),
                ("numero", "codigo_hotel", "Código do Hotel")
            ]):
                continue

            dados_inclusao = {
                "codigo_rede": int(self._extrair_valor(values, 'codigo_rede')),
                "codigo_hotel":
                int(self._extrair_valor(values, 'codigo_hotel')),
            }

            self.close()
            return dados_inclusao

    def mostrar_redes(self, lista_dados_rede):
        string_lista_redes = ""
        for dados_rede in lista_dados_rede:
            string_lista_redes += self.mostrar_rede(dados_rede)

        sg.popup_scrolled(string_lista_redes,
                          title='-------- LISTA DE REDES ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar_rede(self, dados_rede):
        string_dados_rede = ''
        string_dados_rede += "NOME DA REDE: " + str(dados_rede["nome"]) + '\n'
        string_dados_rede += "CÓDIGO DA REDE: " + str(
            dados_rede["codigo"]) + '\n'
        string_dados_rede += "LOCALIZAÇÃO DA REDE: " + str(
            dados_rede["localizacao_rede"]) + '\n'

        if 'hoteis' in dados_rede and dados_rede['hoteis']:
            hoteis = ', '.join(str(h.codigo) for h in dados_rede['hoteis'])
            string_dados_rede += "HOTÉIS: " + hoteis + '\n'
        else:
            string_dados_rede += 'HOTÉIS: Nenhum cadastrado\n'

        string_dados_rede += '\n'
        return string_dados_rede
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Adicionar Rede': 1,
            'Alterar Rede': 2,
            'Listar Rede': 3,
            'Remover Rede': 4,
            'Adicionar Hotel em Rede': 5,
            'Remover Hotel em Rede': 6,
            'Retornar': 7,
            'Cancelar': 0,
            None: 0
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
                  [sg.Button('Adicionar Rede')], [sg.Button('Alterar Rede')],
                  [sg.Button('Listar Rede')], [sg.Button('Remover Rede')],
                  [sg.Button('Adicionar Hotel em Rede')],
                  [sg.Button('Remover Hotel em Rede')],
                  [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def close(self):
        self.__window.Close()
