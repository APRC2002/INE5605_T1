from abc import ABC, abstractmethod


class Pessoa(ABC):
    @property
    @abstractmethod
    def id(self):
        pass
    
    @id.setter
    @abstractmethod
    def id(self, ID):
        pass

    @property
    @abstractmethod
    def nome(self):
        pass
    
    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass
    
    @property
    @abstractmethod
    def data_de_nascimento(self):
        pass
    
    @data_de_nascimento.setter
    @abstractmethod
    def ID(self, data_de_nascimento):
        pass

    @property
    @abstractmethod
    def nacionalidade(self):
        pass
    
    @nacionalidade.setter
    @abstractmethod
    def nacionalidade(self, nacionalidade):
        pass