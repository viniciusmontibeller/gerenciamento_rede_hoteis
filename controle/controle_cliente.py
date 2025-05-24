from limite.tela_cliente import TelaCliente
from controle import ControladorReserva
from entidade.cliente import Cliente


class ControladorCliente():
    def __init__(self, controlador_reserva: ControladorReserva):
        self.__clientes = []
        self.__controlador_reserva = controlador_reserva
        self.__tela_cliente = TelaCliente()
    

    def adicionar(self):
        dados_cliente =  self.__tela_cliente.pega_dados_cliente()
        if self.busca_por_cpf(dados_cliente["cpf"]):
            raise Exception("Cliente ja existente")
        else:
            self.__clientes.append(Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["telefone"], dados_cliente["email"], dados_cliente["fidelidade"]))

    def remover(self):
        cpf = self.__tela_cliente.pega_cpf_cliente()
        cliente_existe = False

        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__clientes.remove(cliente)
                self.__tela_cliente.mosta_mensagem("Removido com sucesso.")
                
                cliente_existe = True
                
                break

        if not cliente_existe:
            raise Exception(f"Cliente com cpf [{cpf}] não foi encontrada para ser removida.")

    def listar(self):
        return map(lambda cliente : {"nome": cliente.nome, "cpf": cliente.cpf, "telefone": cliente.telefone, "email": cliente.email}, self.__clientes)
    
    def alterar(self):
        self.__tela_cliente.mostra_cliente(self.listar())

        dados_cliente =  self.__tela_cliente.pega_dados_cliente()
        cliente_existe = False

        for cliente in self.__clientes:
            if cliente.cpf == dados_cliente["cpf"]:
                self.__clientes[cliente.cpf]["nome"] = dados_cliente["nome"]
                self.__clientes[cliente.cpf]["telefone"] = dados_cliente["telefone"]
                self.__clientes[cliente.cpf]["email"] = dados_cliente["email"]
                
                self.__tela_cliente.mosta_mensagem("Alterado com sucesso.")
                
                cliente_existe = True
                
                break

        if not cliente_existe:
            raise Exception(f"Cliente de cpf [{dados_cliente["cpf"]}] não foi encontrada.")


    def busca_por_cpf(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente

        return None

    def retornar(self):
        self.__controlador_reserva.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar, 2: self.alterar, 3: self.listar, 4: self.remover, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()