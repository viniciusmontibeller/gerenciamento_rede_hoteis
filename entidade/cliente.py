from entidade.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        super().__init__(nome, cpf, telefone, email)
        self.__fidelidade = False

    @property
    def fidelidade(self):
        return self.__fidelidade

    @fidelidade.setter
    def fidelidade(self, fidelidade: bool):
        if isinstance(fidelidade, bool):
            self.__fidelidade = fidelidade
