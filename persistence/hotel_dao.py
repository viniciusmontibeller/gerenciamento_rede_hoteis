from persistence.dao import DAO
from entidade.hotel import Hotel

class HotelDAO(DAO):
    def __init__(self):
        super().__init__('hotel')

    def add(self, hotel: Hotel):
        if((hotel is not None) and isinstance(hotel, Hotel) and isinstance(hotel.codigo, int)):
            super().add(hotel)

    def update(self, hotel: Hotel):
        if((hotel is not None) and isinstance(hotel, Hotel) and isinstance(hotel.codigo, int)):
            super().update(hotel)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)