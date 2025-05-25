from entidade.reserva import Reserva
from limite.tela_reserva import TelaReserva


class ControladorReserva():

    def __init__(self, controlador_sistema):
        self.__reservas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_reserva = TelaReserva()
    
    def adicionar(self):
        dados_reserva = self.__tela_reserva.pega_dados_reserva()
        try:
            cliente = self.__controlador_sistema.controlador_cliente.buscar_por_cpf(dados_reserva["cpf_cliente"])
            hotel = self.__controlador_sistema.controlador_hotel.buscar_por_codigo(dados_reserva["codigo_hotel"])
            quarto = self.__controlador_sistema.controlador_quarto.buscar_por_codigo(dados_reserva["codigo_quarto"])
            funcionario = self.__controlador_sistema.controlador_funcionario.buscar_por_codigo(dados_reserva["codigo_funcionario"])
            
            if self.buscar_por_codigo(dados_reserva["codigo"]):
                raise Exception("Uma reserva com este código já existe.")
            if not cliente:
                raise Exception("Cliente não encontrado")
            if not hotel:
                raise Exception("Hotel não encontrado")
            if not quarto:
                raise Exception("Quarto não encontrado")
            if not funcionario:
                raise Exception("Funcionario não encontrado")

            self.__reservas.append(
                Reserva(dados_reserva["codigo"], cliente, hotel, quarto, funcionario, dados_reserva["data_entrada"], dados_reserva["data_saida"]))
            self.__tela_reserva.mostra_mensagem("Reserva adicionada com sucesso!")
        except Exception as e:
            self.__tela_reserva.mostra_mensagem(str(e))

    def remover(self):
        codigo = self.__tela_rede.pega_codigo_rede()
        try:
            rede_existe = False

            for rede in self.__redes:
                if rede.codigo == codigo:
                    self.__redes.remove(rede)
                    self.__tela_rede.mostra_mensagem("Removido com sucesso.")

                    rede_existe = True

                    break

            if not rede_existe:
                raise Exception(
                    f"Rede de código [{codigo}] não foi encontrada para ser removida."
                )
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def buscar_por_codigo(self, codigo):
        for rede in self.__redes:
            if rede.codigo == codigo:
                return rede

        return None

    def listar(self):
        lista_dados_rede = map(
            lambda rede: {
                "nome": rede.nome,
                "localizacao_rede": rede.localizacao_rede,
                "codigo": rede.codigo,
                "hoteis": rede.hoteis
            }, self.__redes)

        self.__tela_rede.mostrar_redes(lista_dados_rede)

    def alterar(self):
        self.listar()
        dados_rede = self.__tela_rede.pega_dados_rede_para_alteracao()
        
        try:
            rede_existe = False
            for rede in self.__redes:
                if rede.codigo == dados_rede["codigo"]:
                    rede.nome = dados_rede["nome"]
                    rede.localizacao_rede = dados_rede["localizacao_rede"]

                    self.__tela_rede.mostra_mensagem("Alterado com sucesso.")

                    rede_existe = True

                    break

            if not rede_existe:
                raise Exception(
                    f"Rede de código [{dados_rede['codigo']}] não foi encontrada.")
        except Exception as e:
            self.__tela_rede.mostra_mensagem(str(e))

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_reserva.tela_opcoes()]()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()    