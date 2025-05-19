
from entidade.membroAcademia import MembroAcademia
from entidade.filme import Filme

class Voto:
    def __init__(self, votante: MembroAcademia, vencedor: Filme | MembroAcademia):
        if isinstance(votante, MembroAcademia):
            self.__votante = votante
        if isinstance(vencedor, MembroAcademia) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor
    
    @property
    def votante(self) -> MembroAcademia:
        return self.__votante
    
    @votante.setter
    def votante(self, votante: MembroAcademia):
        if isinstance(votante, MembroAcademia):
            self.__votante = votante

    @property
    def vencedor(self)-> Filme | MembroAcademia:
        return self.__vencedor
    
    @vencedor.setter
    def vencedor(self, vencedor: Filme | MembroAcademia):
        if isinstance(vencedor, MembroAcademia) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor
