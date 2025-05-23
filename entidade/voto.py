
from entidade.membroAcademia import MembroAcademia
from entidade.filme import Filme
from entidade.categoria import Categoria

class Voto:
    def __init__(self, votante: MembroAcademia, categoria: Categoria, vencedor: Filme | MembroAcademia):
        if isinstance(votante, MembroAcademia):
            self.__votante = votante
        if isinstance(vencedor, MembroAcademia) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor
        if isinstance(categoria, Categoria):
            self.__categoria = categoria
    
    @property
    def votante(self) -> MembroAcademia:
        return self.__votante
    
    @votante.setter
    def votante(self, votante: MembroAcademia):
        if isinstance(votante, MembroAcademia):
            self.__votante = votante

    @property
    def categoria(self) -> MembroAcademia:
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria: MembroAcademia):
        if isinstance(categoria, MembroAcademia):
            self.__categoria = categoria

    @property
    def votado(self)-> Filme | MembroAcademia:
        return self.__vencedor
    
    @votado.setter
    def votado(self, vencedor: Filme | MembroAcademia):
        if isinstance(vencedor, MembroAcademia) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor
