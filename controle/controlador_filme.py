
from limite.tela_filme import TelaFilme
from entidade.filme import Filme
from entidade.diretor import Diretor
from entidade.ator import Ator


class ControladorFilme():

  def __init__(self, controlador_sistema):
    self.__filmes = []
    self.__tela_filme = TelaFilme()
    self.__controlador_sistema = controlador_sistema

  def pega_filme_por_nome(self, titulo: str):
    for filme in self.__filmes:
      if (filme.titulo == titulo):
        return filme
    return None

  def incluir_filme(self):
    titulo = self.__tela_filme.pega_titulo_filme()
    diretor = self.__controlador_sistema.controlador_diretor.incluir_diretor()
    ator = self.__controlador_sistema.controlador_ator.incluir_ator("M")
    atriz = self.__controlador_sistema.controlador_ator.incluir_ator("F")
    filme = Filme(titulo, diretor, ator, atriz)
    self.__filmes.append(filme)

  def lista_filmes(self):
    for f in self.__filmes:
      categorias = []
      for categoria in f.categorias:
        categorias.append(categoria.nome)
      self.__tela_filme.mostra_filme({"titulo": f.titulo,
                                      "ator": f.ator_principal,
                                      "atriz": f.atriz_principal,
                                      "diretor": f.diretor,
                                      "categorias": categorias})

  def excluir_filme(self):
    self.lista_filmes()
    titulo_filme = self.__tela_filme.seleciona_filme()
    filme = self.pega_filme_por_nome(titulo_filme)
    if (filme is not None):
      self.__filmes.remove(filme)
      self.lista_filmes()
    else:
      self.__tela_filme.mostra_mensagem("ATENÇÃO: filme não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_filme, 2: self.lista_filmes, 3:
                    self.excluir_filme,0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_filme.tela_opcoes()]()
  
  def retorna_filme(self, titulo_do_filme):
    for filme in self.__filmes:
      if filme.titulo == titulo_do_filme:
        return filme

  def inclui_categoria(self, filme, categoria):
    for f in self.__filmes:
      if f.titulo == filme:
        f.adiciona_categoria(categoria)
