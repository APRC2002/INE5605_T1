# teste de commit na web
from membro import Membro
from voto import Voto

class Ator(Membro):
    def __init__(self, ID: int, Nome: str, Data_de_nascimento: str, Nacionalidade: str, genero: str):
        super().__init__(ID, Nome, Data_de_nascimento, Nacionalidade)
        self.__genero = genero

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    
    def votar(self, novo_voto):
        if isinstance(novo_voto, Voto):
            for voto in self.__votos:
                if voto.categoria == novo_voto.categoria:
                    self.__votos.remove(voto)
        self.__votos.append(novo_voto)
