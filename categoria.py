
from filme import Filme
from voto import Voto

class Categoria:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__filmes = []
        self.__votos = []
