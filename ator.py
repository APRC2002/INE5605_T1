
from membro import Membro

class Ator(Membro):
    def __init__(self, ID: str, Nome: str, Data_de_nascimento: str, Nacionalidade: str, genero: str):
        super().__init__(ID, Nome, Data_de_nascimento, Nacionalidade)
        self.__genero = genero

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero