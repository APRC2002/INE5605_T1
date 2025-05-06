
from ator import Ator
from voto import Voto
from filme import Filme
from diretor import Diretor

fernanda_torres = Ator(123, "Fernanda Torres", "01/01/2000", "BR", "F")
selton_mello = Ator(321, "Selton Mello", "01/01/2000", "BR", "M")
fernanda_montenegro = Ator(456, "Fernanda Montenegro", "01/01/1900", "BR", "F")
marjorie_estiano = Ator(456, "Marjorie Estiano", "01/01/2000", "BR", "F")
jackie_chan = Ator(789, "Jackie Chan", "01/01/1960", "CH", "M")
arnold_schwarzenegger = Ator(789, "Arnold Schwarzenegger", "01/01/1960", "AT", "M")
natalie_portman = Ator(456, "Natalie Portman", "01/01/2000", "IL", "F")
tom_cruise = Ator(456, "Tom Cruise", "01/01/2000", "US", "M")

class Estatisticas:
    def __init__(self):
        self.__membros = [fernanda_montenegro, fernanda_torres, selton_mello, marjorie_estiano, arnold_schwarzenegger, jackie_chan, tom_cruise, natalie_portman]

while True:
    print("1. Votar")
    print("2. Vencedor")
    a = int(input("Qual? "))
    if a == 2:
        pass