from entidade.pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        super().__init__(nome, cpf, telefone, email)
