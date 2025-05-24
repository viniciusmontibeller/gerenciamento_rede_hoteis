from limite.tela_funcionario import TelaFuncionario
from controle_hotel import ControladorHotel
from entidade.funcionario import Funcionario


class ControladorFuncionario():
    def __init__(self, controlador_hotel: ControladorHotel):
        self.__funcionarios = []
        self.__controlador_hotel = controlador_hotel
        self.__tela_funcionario = TelaFuncionario()
    

    def adicionar(self):
        dados_funcionario =  self.__tela_funcionario.pega_dados_funcionario()
        if self.busca_por_cpf(dados_funcionario["cpf"]):
            raise Exception("Hotel ja existente")
        else:
            self.__funcionarios.append(Funcionario(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"], dados_funcionario["email"]))

    def remover(self):
        cpf = self.__tela_funcionario.pega_cpf_funcionario()
        funcionario_existe = False

        for funcionario in self.__funcionarios:
            if funcionario.cpf == cpf:
                self.__funcionarios.remove(funcionario)
                self.__tela_funcionario.mosta_mensagem("Removido com sucesso.")
                
                funcionario_existe = True
                
                break

        if not funcionario_existe:
            raise Exception(f"Funcionario com cpf [{cpf}] não foi encontrada para ser removida.")

    def listar(self):
        return map(lambda funcionario : {"nome": funcionario.nome, "cpf": funcionario.cpf, "telefone": funcionario.telefone, "email": funcionario.email}, self.__funcionarios)
    
    def alterar(self):
        self.__tela_funcionario.mostra_funcionario(self.listar())

        dados_funcionario =  self.__tela_funcionario.pega_dados_funcionario()
        funcionario_existe = False

        for funcionario in self.__funcionarios:
            if funcionario.cpf == dados_funcionario["cpf"]:
                self.__funcionarios[funcionario.cpf]["nome"] = dados_funcionario["nome"]
                self.__funcionarios[funcionario.cpf]["telefone"] = dados_funcionario["telefone"]
                self.__funcionarios[funcionario.cpf]["email"] = dados_funcionario["email"]
                
                self.__tela_funcionario.mosta_mensagem("Alterado com sucesso.")
                
                funcionario_existe = True
                
                break

        if not funcionario_existe:
            raise Exception(f"HFuncionario de cpf [{dados_funcionario["cpf"]}] não foi encontrada.")


    def busca_por_cpf(self, cpf):
        for funcionario in self.__funcionarios:
            if funcionario.cpf == cpf:
                return funcionario

        return None

    def retornar(self):
        self.__controlador_hotel.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar, 2: self.alterar, 3: self.listar, 4: self.remover, 0: self.retornar}

        while True:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()