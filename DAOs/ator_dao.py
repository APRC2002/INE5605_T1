from DAOs.dao import DAO
from entidade.ator import Ator

class AtorDAO(DAO):
    def __init__(self):
        super().__init__('at.pkl')

    def add(self, ator: Ator):
        if(ator is not None) and isinstance(ator, Ator):
            super().add(str(ator.id), ator)

    def update(self, ator: Ator):
        if((ator is not None) and isinstance(ator, Ator)):
            super().update(str(ator.id), ator)

    def get(self, key:int):
        return super().get(str(key))

    def remove(self, key:int):
        return super().remove(str(key))