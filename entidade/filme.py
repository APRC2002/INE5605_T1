from entidade.diretor import Diretor
from entidade.ator import Ator
from entidade.membroAcademia import MembroAcademia


class Filme:
    def __init__(self, titulo: str, diretor: Diretor, ator_principal: MembroAcademia, atriz_principal: Ator):
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(diretor, Diretor):
            self.__diretor = diretor
        if isinstance(ator_principal, Ator):
            self.__ator_principal = ator_principal
        if isinstance(atriz_principal, Ator):
            self.__atriz_principal = atriz_principal
        self.__categorias = []
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo
    
    @property
    def diretor(self):
        return self.__diretor
    
    @diretor.setter
    def diretor(self, diretor):
        if isinstance(diretor, Diretor):
            self.__diretor = diretor
    
    @property
    def ator_principal(self):
        return self.__ator_principal
    
    @ator_principal.setter
    def ator_principal(self, ator):
        if isinstance(ator, Ator):
            self.__ator_principal = ator

    @property
    def atriz_principal(self):
        return self.__atriz_principal
    
    @atriz_principal.setter
    def atriz_principal(self, atriz):
        if isinstance(atriz, Ator):
            self.__atriz_principal = atriz
    
    @property
    def categorias(self):
        return self.__categorias

    @categorias.setter
    def categorias(self, categorias):
        self.__categorias = categorias

    def adiciona_categoria(self, categoria):
        self.__categorias.append(categoria)
