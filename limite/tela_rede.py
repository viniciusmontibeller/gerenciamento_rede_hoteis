from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaRede(AbstractTela):
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # def pega_dados_rede(self):
    #     dados_rede = {}
    #     dados_rede["nome"] = input("Nome: ")
    #     dados_rede["codigo"] = super().le_input_so_int("Codigo: ")
    #     dados_rede["localizacao_rede"] = input("Localizacao: ")

    #     return dados_rede
    def pega_dados_rede(self):
        sg.ChangeLookAndFeel('DarkGrey7')
        layout = [
            [sg.Text('-------- DADOS REDE ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(default_text='Ex: IBIS', key='nome', tooltip='Nome da rede')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText(default_text='Ex: 123', key='codigo', tooltip='Apenas números (ex: 123)')],
            [sg.Text('Localização da rede:', size=(15, 1)), sg.InputText(default_text='Ex: Florianopolis', key='localizacao', tooltip='Informe a cidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Genrenciamento de Hoteis e Redes').Layout(layout)
        
        while True:
            button, values = self.__window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None

            nome = values.get("nome", "").strip()
            codigo = values.get("codigo", "").strip()
            localizacao = values.get("localizacao", "").strip()

            if not nome or not codigo or not localizacao:
                sg.popup_error("Todos os campos são obrigatórios. Por favor, preencha todos.")
                continue

            if not codigo.isdigit():
                sg.popup_error("O código deve conter apenas números. Ex: 123")
                continue

            dados_rede = {
                "nome": nome,
                "codigo": codigo,
                "localizacao_rede": localizacao
            }

            self.close()
            return dados_rede

    def pega_dados_rede_para_alteracao(self):
        dados_rede = {}
        dados_rede["codigo"] = super().le_input_so_int("Codigo da rede que será alterada: ")
        dados_rede["nome"] = input("Novo nome: ")
        dados_rede["localizacao_rede"] = input("Nova localização: ")

        return dados_rede

    # def pega_dados_inclusao_de_hotel(self):
    #     dados_inclusao = {}
    #     dados_inclusao["codigo_rede"] = super().le_input_so_int("Código da rede: ")
    #     dados_inclusao["codigo_hotel"] = super().le_input_so_int("Código do hotel que será adicionado na rede: ")

    #     return dados_inclusao
    
    def pega_dados_inclusao_de_hotel(self):
        sg.ChangeLookAndFeel('DarkGrey7')
        layout = [
            [sg.Text('-------- DADOS HOTEL ----------', font=("Helvica", 25))],
            [sg.Text('Código da Rede:', size=(15, 1)), sg.InputText(default_text='Ex: 123', key='codigo_rede', tooltip='Apenas números (ex: 123)')],
            [sg.Text('Código do Hotel:', size=(15, 1)), sg.InputText(default_text='Ex: 123', key='codigo_hotel', tooltip='Apenas números (ex: 123)')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Genrenciamento de Hoteis e Redes').Layout(layout)
        
        while True:
            button, values = self.__window.Read()

            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None

            codigo_rede = values.get("nome", "").strip()
            codigo_hotel = values.get("codigo", "").strip()

            if not codigo_rede or not codigo_hotel:
                sg.popup_error("Todos os campos são obrigatórios. Por favor, preencha todos.")
                continue

            if not codigo_rede.isdigit() and not codigo_hotel.isDigit():
                sg.popup_error("O código deve conter apenas números. Ex: 101")
                continue

            dados_inclusao = {
                "codigo_rede": codigo_rede,
                "codigo_hotel": codigo_hotel,
            }

            self.close()
            return dados_inclusao

    # def mostrar_redes(self, lista_dados_rede):
    #     for dados_rede in lista_dados_rede:
    #         self.mostrar_rede(dados_rede)
    
    def mostrar_redes(self, lista_dados_rede):
        string_lista_redes = ""
        for dados_rede in lista_dados_rede:
            string_lista_redes += self.mostrar_rede(dados_rede)
            
        sg.popup_scrolled(string_lista_redes, title='-------- LISTA DE REDES ----------', font=("Helvetica", 12), size=(60, 20))

    # def mostrar_rede(self, dados_rede):
    #     print("\n")
    #     print("-------- REDES ----------")
    #     print(f"Nome da rede: {dados_rede['nome']}")
    #     print(f"Codigo da rede: {dados_rede['codigo']}")
    #     print(f"Localização da rede: {dados_rede['localizacao_rede']}")
    #     print(f"Hoteis da rede: {', '.join([str(hotel.codigo) for hotel in dados_rede['hoteis']])}")
    #     print("\n")
    
    def mostrar_rede(self, dados_rede):
        string_dados_rede = ''
        string_dados_rede += "NOME DA REDE: " + str(dados_rede["nome"]) + '\n'
        string_dados_rede += "CÓDIGO DA REDE: " + str(dados_rede["codigo"]) + '\n'
        string_dados_rede += "LOCALIZAÇÃO DA REDE: " + str(dados_rede["localizacao_rede"]) + '\n'

        if 'hoteis' in dados_rede and dados_rede['hoteis']:
            hoteis = ', '.join(str(h.codigo) for h in dados_rede['hoteis'])
            string_dados_rede += "HOTÉIS: " + hoteis + '\n'
        else:
            string_dados_rede += 'HOTÉIS: Nenhum cadastrado\n'

        string_dados_rede += '\n'
        return string_dados_rede

    # def pega_codigo_rede(self):
    #     return super().le_input_so_int("Codigo da rede: ")
    
    def pega_codigo_rede(self):
        sg.ChangeLookAndFeel('DarkGrey7')
        layout = [
            [sg.Text('-------- SELECIONAR REDE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código de uma rede que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText(default_text='123', key='codigo', tooltip='Digite apenas números (ex: 123)', size=(20, 1))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona rede').Layout(layout)

        while True:
            button, values = self.__window.Read()
            
            if button in (sg.WIN_CLOSED, 'Cancelar'):
                self.close()
                return None
            
            codigo_str = values.get('codigo', '').strip()
            
            if button == 'Confirmar':
                if not codigo_str.isdigit():
                    sg.popup_error("Por favor, insira apenas números para o código da rede.")
                else:
                    self.close()
                    return str(codigo_str)

    # def mostra_mensagem(self, mensagem):
    #     print(mensagem)
    
    def mostra_mensagem(self, mensagem: str, tipo: str = "info"):
        if tipo == "erro":
            sg.popup_error(mensagem, title="Erro")
        elif tipo == "sucesso":
            sg.popup_ok(mensagem, title="Sucesso")
        elif tipo == "aviso":
            sg.popup_yes_no(mensagem, title="Atenção")
        else:
            sg.popup(mensagem, title="Mensagem")
    
    # def tela_opcoes(self):
    #     print("\n")
    #     print("-------- REDES ----------")
    #     print("Selecione a opção desejada")
    #     print("1 - Adicionar Rede")
    #     print("2 - Alterar Rede")
    #     print("3 - Listar Rede")
    #     print("4 - Remover Rede")
    #     print("5 - Adicionar Hotel em Rede")
    #     print("0 - Retornar")
    #     print("\n")

    #     opcao = super().le_input_int_com_range_de_validacao("Escolha a opcao: ", [0,1,2,3,4,5])
    #     return opcao
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Adicionar Rede': 1,
            'Alterar Rede': 2,
            'Listar Rede': 3,
            'Remover Rede': 4,
            'Adicionar Hotel em Rede': 5,
            'Retornar': 6,
            None: 0,
            'Cancelar': 0,
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkGrey7')
        layout = [
            [sg.Text('Bem vindo ao sistema de gerenciamento de redes e hotéis', font=("Helvetica", 25))],
            [sg.Text('Selecione a opção desejada', font=("Helvica",15))],
            [sg.Button('Adicionar Rede')],
            [sg.Button('Alterar Rede')],
            [sg.Button('Listar Rede')],
            [sg.Button('Remover Rede')],
            [sg.Button('Adicionar Hotel em Rede')],
            [sg.Button('Retornar')]
        ]
        
        self.__window = sg.Window('Genrenciamento de Hoteis e Redes').Layout(layout)

    def close(self):
        self.__window.Close()