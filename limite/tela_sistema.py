from limite.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):
                
    def tela_opcoes(self):
        print("\n")
        print("-------- Sistema de redes de hoteis --------")
        print("Selecione a opção desejada")
        print("1 - Gerenciar Redes")
        print("2 - Gerenciar Hoteis")
        print("3 - Fazer Reserva")
        print("0 - Finalizar sistema")
        print("\n")

        opcao = super().le_input_int_com_range_de_validacao("Opção escolhida: ", [0, 1, 2, 3])
        return opcao