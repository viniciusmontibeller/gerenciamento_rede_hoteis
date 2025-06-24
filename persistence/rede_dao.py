from persistence.dao import DAO
from entidade.rede import Rede

class RedeDAO(DAO):
    def __init__(self):
        super().__init__('rede')

    def add(self, rede: Rede):
        if((rede is not None) and isinstance(rede, rede) and isinstance(rede.codigo, int)):
            super().add(rede)

    def update(self, rede: Rede):
        if((rede is not None) and isinstance(rede, rede) and isinstance(rede.codigo, int)):
            super().update(rede)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def get_all(self):
        return super().get_all()