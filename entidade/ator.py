from entidade.pessoa import Pessoa


class Ator(Pessoa):
    def __init__(self, id: int, nome: str, data_de_nascimento: str, nacionalidade: str, genero: str):
        self.__id = id
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        self.__nacionalidade = nacionalidade
        self.__genero = genero

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento
    
    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
