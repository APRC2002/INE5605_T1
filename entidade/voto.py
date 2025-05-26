
from entidade.membroAcademia import MembroAcademia
from entidade.filme import Filme
from entidade.categoria import Categoria

class Voto:
    def __init__(self, votante: MembroAcademia, categoria: Categoria, votado: Filme):
        if isinstance(votante, MembroAcademia):
            self.__votante = votante
        if isinstance(votado, MembroAcademia) or isinstance(votado, Filme):
            self.__votado = votado
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
        return self.__votado
    
    @votado.setter
    def votado(self, votado: Filme | MembroAcademia):
        if isinstance(votado, MembroAcademia) or isinstance(votado, Filme):
            self.__votado = votado
