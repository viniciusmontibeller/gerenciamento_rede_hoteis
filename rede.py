from hotel import Hotel


class Rede():
    
    def __init__(self, nome: str, cnpj: str, localizacao_sede: str, hoteis: list[Hotel]):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__localizacao_sede = localizacao_sede
        self.__hoteis = hoteis
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
            
    @property
    def localizacao_sede(self):
        return self.__localizacao_sede
    
    @localizacao_sede.setter
    def localizacao_sede(self, localizacao_sede: str):
        if isinstance(localizacao_sede, str):
            self.__localizacao_sede = localizacao_sede
            
     # adicionar checagem de duplicaidade
    def adicionar_hotel(self, hotel: Hotel):
        if isinstance(hotel, Hotel):
            self.__hoteis.append(hotel)
            
    # adicionar checagem de duplicaidade
    def remover_hotel(self, hotel: Hotel):
        if isinstance(hotel, Hotel):
            self.__hoteis.remove(hotel)