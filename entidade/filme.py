
from INE5605_T1.entidade.membroAcademia import Membro

class Filme:
    def __init__(self, titulo: str, diretor: Membro, ator_principal: Membro, atriz_principal: Membro):
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(diretor, Membro):
            if diretor.diretor == True:
                self.__diretor = diretor
        if isinstance(ator_principal, Membro):
            if ator_principal.ator == True:
                self.__ator_principal = ator_principal
        if isinstance(ator_principal, Membro):
            if atriz_principal.ator == True:
                self.__atriz_principal = atriz_principal
    
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
        if isinstance(diretor, Membro):
            if diretor.diretor == True:
                self.__diretor = diretor
    
    @property
    def ator_principal(self):
        return self.__ator_principal
    
    @ator_principal.setter
    def ator_principal(self, ator):
        if isinstance(ator, Membro):
            if ator.ator == True:
                self.__ator_principal = ator

    @property
    def atriz_principal(self):
        return self.__atriz_principal
    
    @atriz_principal.setter
    def atriz_principal(self, atriz):
        if isinstance(atriz, Membro):
            if atriz.ator == True:
                self.__atriz_principal = atriz