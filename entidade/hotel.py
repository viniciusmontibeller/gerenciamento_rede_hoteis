from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from entidade.quarto import Quarto
from entidade.quarto_vip import QuartoVip
from entidade.endereco import Endereco


class Hotel():

    def __init__(self, nome: str, codigo: int, logradouro: str, numero: int,
                 cidade: str, telefone: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__telefone = telefone
        self.__endereco = Endereco(logradouro, numero, cidade)  #composicao
        self.__quartos = []
        self.__funcionarios = []
        self.__clientes = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone

    @property
    def quartos(self):
        return self.__quartos

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def clientes(self):
        return self.__clientes

    def pegar_endereco(self):
        return f"{self.__endereco.logradouro}, número {self.__endereco.numero} em {self.__endereco.cidade}"

    def mudar_endereco(self, logradouro: str, numero: int, cidade: str):
        self.__endereco = Endereco(logradouro, numero, cidade)

    def adicionar_quarto(self, dados_quarto, eh_quarto_vip):
        if eh_quarto_vip:
            quarto = QuartoVip(dados_quarto["numero"],
                               dados_quarto["capacidade"],
                               dados_quarto["preco_diaria"])
        else:
            quarto = Quarto(dados_quarto["numero"], dados_quarto["capacidade"],
                            dados_quarto["preco_diaria"])
        self.__quartos.append(quarto)

    def remover_quarto(self, numero):
        for quarto in self.__quartos:
            if quarto.numero == numero:
                self.__quartos.remove(quarto)
                return quarto

        return None

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)

    def remover_funcionario(self, cpf):
        for funcionario in self.__funcionarios:
            if funcionario.cpf == cpf:
                self.__funcionarios.remove(funcionario)
                return funcionario

        return None

    def adicionar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.clientes.append(cliente)

    def remover_cliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__clientes.remove(cliente)
                return cliente

        return None

    def busca_funcionario_por_cpf(self, cpf):
        for pessoa in self.__funcionarios:
            if pessoa.cpf == cpf:
                return pessoa

        return None

    def busca_cliente_por_cpf(self, cpf):
        for pessoa in self.__clientes:
            if pessoa.cpf == cpf:
                return pessoa

        return None

    def listar_dados_funcionarios(self):
        return map(
            lambda pessoa: {
                "nome": pessoa.nome,
                "cpf": pessoa.cpf,
                "telefone": pessoa.telefone,
                "email": pessoa.email
            }, self.__funcionarios)

    def listar_dados_clientes(self):
        return map(
            lambda pessoa: {
                "nome": pessoa.nome,
                "cpf": pessoa.cpf,
                "telefone": pessoa.telefone,
                "email": pessoa.email
            }, self.__clientes)

    def numero_de_quartos(self):
        return len(self.__quartos)

    def busca_quarto_por_numero(self, numero):
        for quarto in self.__quartos:
            if quarto.numero == numero:
                return quarto

        return None

    def listar_dados_quartos(self):
        return map(
            lambda quarto: {
                "numero": quarto.numero,
                "capacidade": quarto.capacidade,
                "preco_diaria": quarto.preco_diaria
            }, self.__quartos)
