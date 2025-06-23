from limite.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaSistema(AbstractTela):
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()
                
    # def tela_opcoes(self):
    #     print("\n")
    #     print("-------- Sistema de redes de hoteis --------")
    #     print("Selecione a opção desejada")
    #     print("1 - Gerenciar Redes")
    #     print("2 - Gerenciar Hoteis")
    #     print("3 - Fazer Reserva")
    #     print("0 - Finalizar sistema")
    #     print("\n")

    #     opcao = super().le_input_int_com_range_de_validacao("Opção escolhida: ", [0, 1, 2, 3])
    #     return opcao
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, _ = self.__window.Read()

        opcoes = {
            'Gerenciar Redes': 1,
            'Gerenciar Hoteis': 2,
            'Fazer Reserva': 3,
            'Finalizar sistema': 0,
            None: 0,
            'Cancelar': 0,
        }

        opcao = opcoes.get(button, 0)
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()
        
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkGrey7')
        layout = [
            [sg.Text('Bem vindo ao sistema de gerenciamento de redes e hotéis', font=("Helvetica", 25))],
            [sg.Text('Selecione a opção desejada', font=("Helvica",15))],
            [sg.Button('Gerenciar Redes')],
            [sg.Button('Gerenciar Hoteis')],
            [sg.Button('Fazer Reserva')],
            [sg.Button('Finalizar sistema')]
        ]
        
        self.__window = sg.Window('Genrenciamento de Hoteis e Redes').Layout(layout)