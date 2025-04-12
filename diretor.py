
from membro import Membro

class Diretor(Membro):
    def __init__(self, ID: str, Nome: str, Data_de_nascimento: str, Nacionalidade: str):
        super().__init__(ID, Nome, Data_de_nascimento, Nacionalidade)
