from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg
from limite.enum.input_data_type import InputDataType
from datetime import datetime


class TelaReserva(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Adicionar Reserva': 1,
            'Alterar Reserva': 2,
            'Listar Reserva': 3,
            'Remover Reserva': 4,
            'Retornar': 0,
            None: 0,
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Gerenciamento de reservas', font=("Helvetica", 25))],
            [sg.Text('Selecione a opção desejada', font=("Helvica", 15))],
            [sg.Button('Adicionar Reserva')], [sg.Button('Alterar Reserva')],
            [sg.Button('Listar Reserva')], [sg.Button('Remover Reserva')],
            [sg.Button('Retornar')]
        ]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_reserva(self):

        schema = {
            "title":
            "DADOS RESERVA",
            "fieldList": [{
                "label": "Código do hotel",
                "key": "codigo_hotel",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "Número do quarto",
                "key": "numero_quarto",
                "tooltip": "Apenas números (ex: 123)",
                "isRequired": True,
                "dataType": InputDataType.NUMERO,
                "parseAs": int
            }, {
                "label": "CPF do cliente",
                "key": "cpf_cliente",
                "tooltip":
                "CPF deve conter apenas numeros e ter exatamente 11 digitos",
                "isRequired": True,
                "dataType": InputDataType.CPF,
                "parseAs": str
            }, {
                "label": "CPF do funcionario",
                "key": "cpf_funcionario",
                "tooltip":
                "CPF deve conter apenas numeros e ter exatamente 11 digitos",
                "isRequired": True,
                "dataType": InputDataType.CPF,
                "parseAs": str
            }, {
                "label": "Data de entrada",
                "key": "data_entrada",
                "tooltip": "Data no formato (DD-MM-YYYY)",
                "isRequired": True,
                "dataType": InputDataType.DATA,
                "parseAs": str
            }, {
                "label": "Data de saida",
                "key": "data_saida",
                "tooltip": "Data no formato (DD-MM-YYYY)",
                "isRequired": True,
                "dataType": InputDataType.DATA,
                "parseAs": str
            }]
        }

        dados = self._pega_dados(schema)

        dados["data_entrada"] = datetime.strptime(dados["data_entrada"],
                                                  "%d-%m-%Y")
        dados["data_saida"] = datetime.strptime(dados["data_saida"],
                                                "%d-%m-%Y")

        return dados

    def mostrar_reservas(self, lista_dados_reserva):
        string_lista_reserva = ""
        for dados_reserva in lista_dados_reserva:
            string_lista_reserva += self.mostrar_reserva(dados_reserva)

        sg.popup_scrolled(string_lista_reserva,
                          title='-------- LISTA DE RESERVAS ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar_reserva(self, dados_reserva):
        string_dados_reservas = ''
        string_dados_reservas += "Código da reserva: " + str(
            dados_reserva['codigo']) + '\n'
        string_dados_reservas += "Cliente da reserva: " + str(
            dados_reserva['cliente']) + '\n'
        string_dados_reservas += "Hotel da reserva: " + str(
            dados_reserva['hotel']) + '\n'
        string_dados_reservas += "Quarto da reserva: " + str(
            dados_reserva['quarto']) + '\n'
        string_dados_reservas += "Funcionário responsável: " + str(
            dados_reserva['funcionario']) + '\n'
        string_dados_reservas += "Data de entrada: " + str(
            dados_reserva['data_entrada']) + '\n'
        string_dados_reservas += "Data de saída: " + str(
            dados_reserva['data_saida']) + '\n'
        string_dados_reservas += "Status da reserva: " + str(
            dados_reserva['status'].value) + '\n'
        string_dados_reservas += "Custo da reserva: R$" + str(
            dados_reserva['custo']) + '\n'

        string_dados_reservas += '\n'
        return string_dados_reservas

    def close(self):
        self.__window.Close()
