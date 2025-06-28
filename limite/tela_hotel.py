from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
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
                  [sg.Button('Gerenciar Funcionários de um Hotel')],
                  [sg.Button('Gerenciar Clientes de um Hotel')],
                  [sg.Button('Gerenciar Quartos de um Hotel')],
                  [sg.Button('Incluir Hotel')], [sg.Button('Alterar Hotel')],
                  [sg.Button('Listar Hoteis')], [sg.Button('Excluir Hoteis')],
                  [sg.Button('Relatório Geral de Hoteis')],
                  [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_hotel(self):
        schema = {
            "title":
            "DADOS HOTEL",
            "fieldList": [{
                "label": "Nome",
                "key": "nome",
                "tooltip": "Nome",
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
                "label": "Endereço",
                "key": "endereco",
                "tooltip": "Informe o endereço",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }, {
                "label": "Telefone",
                "key": "telefone",
                "tooltip": "Informe o telefone",
                "isRequired": True,
                "dataType": InputDataType.TELEFONE,
                "parseAs": str
            }]
        }

        return self._pega_dados(schema)

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
        string_lista = ""

        for dados_hotel in lista_dados_hoteis:
            string_lista += "Nome do hotel: " + str(dados_hotel["nome"]) + "\n"
            string_lista += "Código do hotel: " + str(
                dados_hotel["codigo"]) + "\n"
            string_lista += "Funcionários do hotel: " + str(
                dados_hotel["numero_funcionarios"]) + "\n"
            string_lista += "Clientes do hotel: " + str(
                dados_hotel["numero_clientes"]) + "\n"
            string_lista += "Quartos do hotel: " + str(
                dados_hotel["numero_quartos"]) + "\n"
            string_lista += "Número de reservas: " + str(
                dados_hotel["numero_reservas"]) + "\n"
            string_lista += "Faturamento total em reservas: + " + str(
                dados_hotel["faturamento_total_em_reservas"]) + "\n"
            string_lista += "\n"

        sg.popup_scrolled(string_lista,
                          title="-------- Relatório Geral de Hoteis --------",
                          font=("Helvetica", 12),
                          size=(60, 20))

    def close(self):
        self.__window.Close()
