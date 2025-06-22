from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from excecoes.lista_vazia_exception import ListaVaziaException


class ControladorCliente():
    def __init__(self, controlador_hotel):
        self.__controlador_hotel = controlador_hotel
        self.__tela_cliente = TelaCliente()

    def adicionar(self):
        try:
            codigo_hotel = self.__tela_cliente.pega_codigo_hotel()
            dados_cliente = self.__tela_cliente.pega_dados_cliente()
            hotel = self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel)
        
            if self.busca_por_cpf(hotel, dados_cliente["cpf"]):
                raise Exception("Cliente ja existente")
            hotel.clientes.append(
                Cliente(dados_cliente["nome"],
                            dados_cliente["cpf"],
                            dados_cliente["telefone"],
                            dados_cliente["email"]))
            self.__tela_cliente.mostra_mensagem("Cliente adicionado com sucesso!")
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))

    def remover(self):
        codigo_hotel = self.__tela_cliente.pega_codigo_hotel()
        if not self.listar(codigo_hotel):
                return
        
        cpf = self.__tela_cliente.pega_cpf_cliente()
        
        try:
            cliente_existe = False
            for cliente in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).clientes:
                if cliente.cpf == cpf:
                    for reserva in self.__controlador_hotel.controlador_sistema.controlador_reserva.listar_reservas_por_hotel(codigo_hotel):
                        if reserva.cliente.cpf == cpf:
                            raise Exception("Não é possível remover um cliente que ja possui reserva.")
                        
                    self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).clientes.remove(cliente)
                    self.__tela_cliente.mostra_mensagem("Removido com sucesso.")
                    cliente_existe = True
                    break

            if not cliente_existe:
                raise Exception(
                    f"Cliente com cpf [{cpf}] não foi encontrada para ser removida."
                )
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))

    def listar(self, codigo_hotel = None):
        try:
            if not codigo_hotel:
                codigo_hotel = self.__tela_cliente.pega_codigo_hotel()
            if not len(self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).clientes) >= 1:
                raise ListaVaziaException('clientes')
            
            lista_dados_cliente = map(
                lambda cliente: {
                    "nome": cliente.nome,
                    "cpf": cliente.cpf,
                    "telefone": cliente.telefone,
                    "email": cliente.email
                }, self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).clientes)
            
            self.__tela_cliente.mostrar_clientes(lista_dados_cliente)
            return True
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))
        except ListaVaziaException as e:
            self.__tela_funcionario.mostra_mensagem(str(e))
            return False

    def alterar(self):
        codigo_hotel = self.__tela_cliente.pega_codigo_hotel()
        if not self.listar(codigo_hotel):
            return

        dados_cliente = self.__tela_cliente.pega_dados_cliente()

        try:
            cliente_existe = False
            for cliente in self.__controlador_hotel.busca_hotel_por_codigo(codigo_hotel).clientes:
                if cliente.cpf == dados_cliente["cpf"]:
                    cliente.nome = dados_cliente["nome"]
                    cliente.telefone = dados_cliente["telefone"]
                    cliente.email = dados_cliente["email"]
                    self.__tela_cliente.mostra_mensagem("Alterado com sucesso.")
                    cliente_existe = True
                    break

            if not cliente_existe:
                raise Exception(
                    f"Cliente de cpf [{dados_cliente['cpf']}] não foi encontrada."
                )
        except Exception as e:
            self.__tela_cliente.mostra_mensagem(str(e))

    def busca_por_cpf(self, hotel, cpf):
        for cliente in hotel.clientes:
            if cliente.cpf == cpf:
                return cliente

        return None

    def retornar(self):
        self.__controlador_hotel.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar,
            2: self.alterar,
            3: self.listar,
            4: self.remover,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
