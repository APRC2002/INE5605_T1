from DAOs.dao import DAO
from entidade.diretor import Diretor

class DiretorDAO(DAO):
    def __init__(self):
        super().__init__('dir.pkl')

    def add(self, diretor: Diretor):
        if(diretor is not None) and isinstance(diretor, Diretor):
            super().add(str(diretor.id), diretor)

    def update(self, diretor: Diretor):
        if((diretor is not None) and isinstance(diretor, Diretor)):
            super().update(str(diretor.id), diretor)

    def get(self, key: int):
        return super().get(str(key))

    def remove(self, key: int):
        return super().remove(str(key)) 