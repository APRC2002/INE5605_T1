
from membro import Membro
from filme import Filme

class Voto:
    def __init__(self, votante: Membro, vencedor: Filme | Membro):
        if isinstance(votante, Membro):
            self.__votante = votante
        if isinstance(vencedor, Membro) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor
    
    @property
    def votante(self):
        return self.__votante
    
    @votante.setter
    def votante(self, votante):
        if isinstance(votante, str):
            self.__votante = votante

    @property
    def vencedor(self):
        return self.__vencedor
    
    @vencedor.setter
    def vencedor(self, vencedor):
        if isinstance(vencedor, Membro) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor