from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import PySimpleGUI as sg


class TelaFuncionario(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Funcionario': 1,
            'Alterar Funcionario': 2,
            'Listar Funcionarios': 3,
            'Remover Funcionario': 4,
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
                  [sg.Button('Incluir Funcionario')],
                  [sg.Button('Alterar Funcionario')],
                  [sg.Button('Listar Funcionarios')],
                  [sg.Button('Remover Funcionario')], [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_funcionario(self):
        schema = {
            "title":
            "DADOS FUNCIONARIO",
            "fieldList": [{
                "label": "Nome",
                "key": "nome",
                "tooltip": "Nome",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }, {
                "label": "CPF",
                "key": "cpf",
                "tooltip": "Apenas números (ex: 12645972900)",
                "isRequired": True,
                "dataType": InputDataType.CPF,
                "parseAs": str
            }, {
                "label": "Email",
                "key": "email",
                "tooltip": "Informe o email (ex.: tiagossansao@gmail.com)",
                "isRequired": True,
                "dataType": InputDataType.TEXTO,
                "parseAs": str
            }, {
                "label": "Telefone",
                "key": "telefone",
                "tooltip": "Informe o telefone (Ex.: 47988303706)",
                "isRequired": True,
                "dataType": InputDataType.TELEFONE,
                "parseAs": str
            }]
        }

        return self._pega_dados(schema)

    def mostrar_funcionarios(self, lista_dados):
        string_lista = ""
        for dados in lista_dados:
            string_lista += self.mostrar(dados)

        sg.popup_scrolled(string_lista,
                          title='-------- Listagem de Funcionários ----------',
                          font=("Helvetica", 12),
                          size=(60, 20))

    def mostrar(self, dados):
        string_dados = ""
        string_dados += "Nome do funcionário: " + str(dados["nome"]) + "\n"
        string_dados += "CPF do funcionário: " + str(dados["cpf"]) + "\n"
        string_dados += "Telefone do funcionário: " + str(
            dados["telefone"]) + "\n"
        string_dados += "Email do funcionário: " + str(dados["email"]) + "\n"
        string_dados += '\n'

        return string_dados

    def close(self):
        self.__window.Close()
