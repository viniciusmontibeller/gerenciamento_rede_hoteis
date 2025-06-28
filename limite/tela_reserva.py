from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaReserva(AbstractTela):

    def pega_dados_reserva(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('DADOS RESERVA', font=("Helvica", 20), justification="center")],
            [sg.Text('Códido do hotel', size=(15, 1)), sg.InputText(key='codigo_hotel', tooltip='Apenas números (ex: 123)')],
            [sg.Text('Número do quarto', size=(15, 1)), sg.InputText(key='numero_quarto', tooltip='Apenas números (ex: 123)')],
            [sg.Text('CPF do cliente:', size=(15, 1)), sg.InputText(key='cpf_cliente', tooltip='Apenas números (ex: 123)')],
            [sg.Text('CPF do funcionario', size=(15, 1)), sg.InputText(key='cpf_funcionario', tooltip='Apenas números (ex: 123)')],
            [sg.Text('Data de entrada (DD-MM-YYYY)', size=(15, 1)), sg.InputText(key='data_entrada', tooltip='Data no formato (DD-MM-YYYY)')],
            [sg.Text('Data de saida (DD-MM-YYYY)', size=(15, 1)), sg.InputText(key='data_saida', tooltip='Data no formato (DD-MM-YYYY)')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
            
        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)
        
        while True:
            button, values = self.__window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None
            
            if not self._validar_campos(values, [
                    ("obrigatorio", "codigo_hotel", "Códido do hotel"),
                    ("numero", "codigo_hotel", "Códido do hotel"),
                    ("obrigatorio", "numero_quarto", "Número do quarto"),
                    ("numero", "numero_quarto", "Número do quarto"),
                    ("obrigatorio", "cpf_cliente", "CPF do cliente"),
                    ("cpf", "cpf_cliente", "CPF do cliente"),
                    ("obrigatorio", "cpf_funcionario", "CPF do funcionario"),
                    ("cpf", "cpf_funcionario", "CPF do funcionario"),
                    ("obrigatorio", "data_entrada", "Data de entrada"),
                    ("data", "data_entrada", "Data de entrada"),
                    ("obrigatorio", "data_saida", "Data de saida"),
                    ("data", "data_saida", "Data de saida"),
                    ("data_saida", "data_saida", "Data de saida"),
                ]):
                continue
            

            dados_reserva = {
                "codigo_hotel": int(self._extrair_valor(values, 'codigo_hotel')),
                "numero_quarto": int(self._extrair_valor(values, 'numero_quarto')),
                "cpf_cliente": int(self._extrair_valor(values, 'cpf_cliente')),
                "cpf_funcionario": int(self._extrair_valor(values, 'cpf_funcionario')),
                "data_entrada": self._extrair_valor(values, 'data_entrada'),
                "data_saida": self._extrair_valor(values, 'data_saida')
            }

            self.close()
            return dados_reserva

    def mostrar_reservas(self, lista_dados_reserva):
        string_lista_reserva = ""
        for dados_reserva in lista_dados_reserva:
            string_lista_reserva += self.mostrar_rede(dados_reserva)
            
        sg.popup_scrolled(string_lista_reserva, title='-------- LISTA DE RESERVAS ----------', font=("Helvetica", 12), size=(60, 20))
    
    def mostrar_reserva(self, dados_reserva):
        string_dados_reservas = ''
        string_dados_reservas += "CÓDIGO DA RESERVA: " + str(dados_reserva['codigo']) + '\n'
        string_dados_reservas += "CLIENTE DA RESERVA: " + str(dados_reserva['cliente']) + '\n'
        string_dados_reservas += "HOTEL DA RESERVA: " + str(dados_reserva['hotel']) + '\n'
        string_dados_reservas += "QUARTO DA RESERVA: " + str(dados_reserva['quarto']) + '\n'
        string_dados_reservas += "FUNCIONÁRIO RESPONSÁVEL: " + str(dados_reserva['funcionario']) + '\n'
        string_dados_reservas += "DATA DE ENTRADA: " + str(dados_reserva['data_entrada']) + '\n'
        string_dados_reservas += "DATA DE SAÍDA: " + str(dados_reserva['data_saida']) + '\n'
        string_dados_reservas += "STATUS DA RESERVA: " + str(dados_reserva['status'].value) + '\n'
        string_dados_reservas += "CUSTO DA RESERVA: R$" + str(dados_reserva['custo']) + '\n'

        string_dados_reservas += '\n'
        return string_dados_reservas

    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Adicionar Reserva': 1,
            'Alterar Reserva': 2,
            'Listar Reserva': 3,
            'Remover Reserva': 4,
            'Retornar': 5,
            None: 0,
            'Cancelar': 0,
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme(self.ESTILO_JANELA)
        layout = [
            [sg.Text('Gerenciamento de reservas', font=("Helvetica", 25))],
            [sg.Text('Selecione a opção desejada', font=("Helvica",15))],
            [sg.Button('Adicionar Reserva')],
            [sg.Button('Alterar Reserva')],
            [sg.Button('Listar Reserva')],
            [sg.Button('Remover Reserva')],
            [sg.Button('Retornar')]
        ]
        
        self.__window = sg.Window(self.TITULO_BASE).Layout(layout)

    def close(self):
        self.__window.Close()
