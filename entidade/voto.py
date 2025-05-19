
from entidade.membroAcademia import MembroAcademia
from entidade.filme import Filme

class Voto:
    def __init__(self, votante: MembroAcademia, vencedor: Filme | MembroAcademia):
        if isinstance(votante, MembroAcademia):
            self.__votante = votante
        if isinstance(vencedor, MembroAcademia) or isinstance(vencedor, Filme):
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
        if isinstance(vencedor, MembroAcademia) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor