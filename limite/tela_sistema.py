class TelaSistema():
    
    def tela_opcoes(self):
        print("-------- Sistema de redes de hoteis --------")
        print("Selecione a opção desejada")
        print("1 - Gerenciar Redes")
        print("2 - Gerenciar Hoteis")
        print("3 - Fazer Reserva")
        print("0 - Finalizar sistema")

        opcao = input("Opção escohida")  # Falta adicionar verificação de input de usuario
        
        return opcao