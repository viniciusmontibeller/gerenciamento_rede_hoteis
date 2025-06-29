from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import PySimpleGUI as sg


class TelaQuarto(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Quarto': 1,
            'Alterar Quarto': 2,
            'Listar Quartos': 3,
            'Excluir Quartos': 4,
            'Retornar': 5,
            'Cancelar': 0,
            None: 0
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[
            sg.Text('Gerenciamento de quartos',
                    font=("Helvetica", 25))
        ], [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
            [sg.Button('Incluir Quarto')],
            [sg.Button('Alterar Quarto')],
            [sg.Button('Listar Quartos')],
            [sg.Button('Excluir Quartos')],
            [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_quarto(self):
        schema = {
            "title":
                "DADOS QUARTO",
                "fieldList": [{
                    "label": "Número",
                    "key": "numero",
                    "tooltip": "Apenas números (ex: 123).",
                    "isRequired": True,
                    "dataType": InputDataType.NUMERO,
                    "parseAs": int
                }, {
                    "label": "Capacidade",
                    "key": "capacidade",
                    "tooltip": "Apenas números (ex: 123)",
                    "isRequired": True,
                    "dataType": InputDataType.NUMERO,
                    "parseAs": int
                }, {
                    "label": "Preço da diaria(R$)",
                    "key": "preco_diaria",
                    "tooltip": "Preço da diaria em Reais",
                    "isRequired": True,
                    "dataType": InputDataType.FLOAT,
                    "parseAs": float
                }]
        }

        return self._pega_dados(schema)

    def pega_eh_quarto_vip(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text("TIPO DE QUARTO", font=("Helvica", 20), justification="center")],
            [sg.Text("Escolha o tipo do quarto", font=("Helvica", 15))],
            [sg.Radio("Normal", group_id="tipo_quarto", key="normal", default=True),
            sg.Radio("Vip", group_id="tipo_quarto", key="vip")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window(self.TITULO_BASE, layout)

        while True:
            button, values = window.read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            window.close()
            if values["vip"]:
                return True
            else:
                return False

    def mostrar_quartos(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- LISTA DE QUARTOS ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "NÚMERO DO QUARTO: " + str(dados["numero"]) + "\n"
        string_dados += "CAPACIDADE: " + str(dados["capacidade"]) + "\n"
        string_dados += "PRECO DA DIARIA" + str(dados["preco_diaria"]) + "\n"
        string_dados += '\n'

        return string_dados

    def pega_numero_quarto(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [[
            sg.Text('SELECIONAR QUARTO', font=("Helvica", 20), justification='center')
        ], [
            sg.Text(f'Digite o numero do quarto', font=("Helvica", 15))
        ],
                  [
                      sg.Text(f'Número do quarto:', size=(15, 1)),
                      sg.InputText(key='numero',
                                   tooltip='Digite apenas números (ex: 123)',
                                   size=(20, 1))
                  ], [sg.Button('Confirmar'),
                      sg.Cancel('Cancelar')]]
        window = sg.Window(self.TITULO_BASE).Layout(layout)

        while True:
            button, values = window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                window.Close()
                return None

            if not self._validar_campos(values,
                                        [("obrigatorio", "numero", "Número"),
                                         ("numero", "numero", "Número")]):
                continue

            window.Close()
            return int(self._extrair_valor(values, 'codigo'))

    def close(self):
        self.__window.Close()
