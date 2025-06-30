from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg
from limite.enum.input_data_type import InputDataType


class TelaRede(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

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
        layout = [
            [sg.Text('Gerenciamento de redes', font=("Helvetica", 25))],
            [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
            [sg.Button('Adicionar Rede')], [sg.Button('Alterar Rede')],
            [sg.Button('Listar Rede')], [sg.Button('Remover Rede')],
            [sg.Button('Adicionar Hotel em Rede')],
            [sg.Button('Remover Hotel em Rede')], [sg.Button('Retornar')]
        ]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_rede(self):
        schema = {
            "title":
            "DADOS REDE",
            "fieldList": [{
                "label": "Nome",
                "key": "nome",
                "tooltip": "Nome da Rede",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }, {
                "label": "Código",
                "key": "codigo",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "Localização da rede",
                "key": "localizacao_rede",
                "tooltip": "Informe a cidade origem da rede",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }]
        }

        return self._pega_dados(schema)

    def pega_dados_inclusao_de_hotel(self):
        schema = {
            "title":
            "INCLUSAO DE HOTEL EM REDE",
            "fieldList": [{
                "label": "Código da Rede",
                "key": "codigo_rede",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "Código do Hotel",
                "key": "codigo_hotel",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }]
        }

        return self._pega_dados(schema)

    def pega_dados_remover_hotel(self):
        schema = {
            "title":
            "REMOVER HOTEL DA REDE",
            "fieldList": [{
                "label": "Código da Rede",
                "key": "codigo_rede",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "Código do Hotel",
                "key": "codigo_hotel",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }]
        }

        return self._pega_dados(schema)

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

    def close(self):
        self.__window.Close()
