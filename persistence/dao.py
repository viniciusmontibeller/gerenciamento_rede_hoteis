import pickle
from abc import ABC, abstractmethod
from excecoes.nao_encontrado_exception import NaoEncontradoException

class DAO(ABC):
    @abstractmethod
    def __init__(self, entity_name='', entity_identifier='codigo'):
        default_dir = "pickle_files"

        self.__datasource = f'{default_dir}/{entity_name}.pkl'
        self.__cache = []
        self.__entity_name = entity_name
        self.__identifier = entity_identifier
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, obj):
        self.__cache.append(obj)
        self.__dump()

    def update(self, obj):
        for entity in self.__cache:
            if entity[self.__identifier] == obj[self.__identifier]:
                entity[self.__identifier] = obj
                self.__dump()
                return entity
        
        raise NaoEncontradoException(self.__entity_name, self.__identifier, obj[self.__identifier])


    def get(self, key):
        for entity in self.__cache:
            if entity[self.__identifier] == key:
                return entity

        raise NaoEncontradoException(self.__entity_name, self.__identifier, key)

    def remove(self, key):
        for entity in self.__cache:
            if entity[self.__identifier] == key:
                self.__cache.remove(entity)    
                self.__dump()
                return entity

        raise NaoEncontradoException(self.__entity_name, self.__identifier, key)
        
    def get_all(self):
        return self.__cache
