
from abc import ABC, abstractmethod
from voto import Voto

class Membro:
    @abstractmethod
    def __init__(self, ID: int, Nome: str, Data_de_nascimento: str, Nacionalidade: str):
        self.__ID = ID
        self.__nome = Nome
        self.__data_de_nascimento = Data_de_nascimento
        self.__nacionalidade = Nacionalidade
        self.__votos = []

    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, ID):
        self.__ID = ID

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
    def ID(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade
    
    @abstractmethod
    def votar(self, novo_voto):
        if isinstance(novo_voto, Voto):
            for voto in self.__votos:
                if voto.categoria == novo_voto.categoria:
                    self.__votos.remove(voto)
        self.__votos.append(novo_voto)
