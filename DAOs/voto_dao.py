from DAOs.dao import DAO
from entidade.voto import Voto

class VotoDAO(DAO):
    def __init__(self):
        super().__init__('vot.pkl')

    def add(self, voto: Voto):
        if(voto is not None) and isinstance(voto, Voto):
            key = f"{voto.votante.id}_{voto.categoria.nome}"
            super().add(key, voto)

    def update(self, voto: Voto):
        if((voto is not None) and isinstance(voto, Voto)):
            key = f"{voto.votante.id}_{voto.categoria.nome}"
            super().update(key, voto)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key) 