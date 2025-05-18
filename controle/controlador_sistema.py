from limite.tela_sistema import TelaSistema
from controle.controlador_membroAcademia import ControladorMembroAcademia
from controle.controlador_ator import ControladorAtor
from controle.controlador_diretor import ControladorDiretor
from controle.controlador_filme import ControladorFilme
from controle.controlador_categoria import ControladorCategoria
#from controle.controlador_votacao import ControladorVotacao

class ControladorSistema:

    def __init__(self):
        self.__controlador_membroAcademia = ControladorMembroAcademia(self)
        self.__controlador_ator = ControladorAtor(self)
        self.__controlador_diretor = ControladorDiretor(self)
        self.__controlador_filme = ControladorFilme(self)
        self.__controlador_categoria = ControladorCategoria(self)
        #self.__controlador_votacao = ControladorVotacao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_membroAcademia(self):
        return self.__controlador_membroAcademia
    
    @property
    def controlador_ator(self):
        return self.__controlador_ator
    
    @property
    def controlador_diretor(self):
        return self.__controlador_diretor
    
    @property
    def controlador_filme(self):
        return self.__controlador_filme
    
    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    #@property
    #def controlador_votacao(self):
    #    return self.__controlador_votacao

    

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_membroAcademia(self):
        # Chama o controlador de MembroAcademia
        self.__controlador_membroAcademia.abre_tela()

    def cadastra_ator(self):
        # Chama o controlador de Ator
        self.__controlador_ator.abre_tela()

    def cadastra_diretor(self):
        # Chama o controlador de Diretor
        self.__controlador_diretor.abre_tela()

    def cadastra_filme(self):
        # Chama o controlador de Filme
        self.__controlador_filme.abre_tela()

    def cadastra_categoria(self):
        # Chama o controlador de Categoria
        self.__controlador_categoria.abre_tela()

    #def cadastra_votacao(self):
        # Chama o controlador de Votacao
    #    self.__controlador_votacao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_membroAcademia, 2: self.cadastra_ator, 3: self.cadastra_diretor, 4: self.cadastra_filme, 
                        5: self.cadastra_categoria, 0: self.encerra_sistema} #6: self.cadastra_votacao

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()