
from limite.tela_filme import TelaFilme
from entidade.filme import Filme
from entidade.diretor import Diretor
from entidade.ator import Ator
import time

def current_milli_time():
  return round(time.time() * 10)

def cria_id():
  return str(current_milli_time() - 17481983713)


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
    diretor = self.__controlador_sistema.controlador_diretor.incluir_diretor(cria_id())
    ator = self.__controlador_sistema.controlador_ator.incluir_ator("M", cria_id())
    atriz = self.__controlador_sistema.controlador_ator.incluir_ator("F", cria_id())
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
      ator = filme.ator_principal
      atriz = filme.atriz_principal
      diretor = filme.diretor
      for a in self.__controlador_sistema.controlador_ator.atores:
        if a.id == ator.id:
          self.__controlador_sistema.controlador_ator.excluir_ator_por_id(a.id)
      for a in self.__controlador_sistema.controlador_ator.atores:
        if a.id == atriz.id:
          self.__controlador_sistema.controlador_ator.excluir_ator_por_id(a.id)
      for d in self.__controlador_sistema.controlador_diretor.diretores:
        if d.id == diretor.id:
          self.__controlador_sistema.controlador_diretor.excluir_diretor_por_id(d.id)
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
      if f.titulo == filme and categoria not in f.categorias:
        f.adiciona_categoria(categoria)
