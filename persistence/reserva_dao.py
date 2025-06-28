from persistence.dao import DAO
from entidade.reserva import Reserva

class ReservaDAO(DAO):
    def __init__(self):
        super().__init__('reserva')

    def add(self, reserva: Reserva):
        if((reserva is not None) and isinstance(reserva, Reserva) and isinstance(reserva.codigo, int)):
            super().add(reserva)

    def update(self, reserva: Reserva):
        if((reserva is not None) and isinstance(reserva, Reserva) and isinstance(reserva.codigo, int)):
            super().update(reserva)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def get_all(self):
        return super().get_all()