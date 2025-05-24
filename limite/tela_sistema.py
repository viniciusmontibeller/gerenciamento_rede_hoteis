from abstract_tela import AbstractTela

class TelaSistema(AbstractTela):
                
    def tela_opcoes(self):
        print("-------- Sistema de redes de hoteis --------")
        print("Selecione a opção desejada")
        print("1 - Gerenciar Redes")
        print("2 - Gerenciar Hoteis")
        print("3 - Fazer Reserva")
        print("0 - Finalizar sistema")

        opcao = super().le_input_int("Opção escohida: ", [0,1,2,3])
        return opcao