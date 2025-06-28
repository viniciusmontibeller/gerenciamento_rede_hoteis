from limite.abstract_tela import AbstractTela
from limite.enum.input_data_type import InputDataType
import PySimpleGUI as sg


class TelaCliente(AbstractTela):

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Incluir Cliente': 1,
            'Alterar Cliente': 2,
            'Listar Clientes': 3,
            'Remover Cliente': 4,
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
        ], [sg.Text('Selecione a opção desejada',
                    font=("Helvica", 15))], [sg.Button('Incluir Cliente')],
                  [sg.Button('Alterar Cliente')],
                  [sg.Button('Listar Clientes')],
                  [sg.Button('Remover Cliente')], [sg.Button('Retornar')]]

        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def pega_dados_cliente(self):
        schema = {
            "title":
            "DADOS CLIENTE",
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

    def mostrar_clientes(self, lista_dados_cliente):
        print("\n")
        print("-------- Listagem de Clientes --------")
        print("\n")
        for dados_cliente in lista_dados_cliente:
            self.mostra_cliente(dados_cliente)

    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF do cliente: ", dados_cliente["cpf"])
        print("Telefone do cliente: ", dados_cliente["telefone"])
        print("Email do cliente: ", dados_cliente["email"])
        print("\n")

    def close(self):
        self.__window.Close()
