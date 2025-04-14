
from ator import Ator
from diretor import Diretor
from filme import Filme


class Voto:
    def __init__(self, categoria: str, vencedor: Filme | Ator | Diretor):
        if isinstance(categoria, str):
            self.__categoria = categoria
        if isinstance(vencedor, Ator) or isinstance(vencedor, Diretor) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        if isinstance(categoria, str):
            self.__categoria = categoria

    @property
    def vencedor(self):
        return self.__vencedor
    
    @vencedor.setter
    def vencedor(self, vencedor):
        if isinstance(vencedor, Ator) or isinstance(vencedor, Diretor) or isinstance(vencedor, Filme):
            self.__vencedor = vencedor