from limite.tela_filme import TelaFilme
from entidade.filme import Filme
from entidade.diretor import Diretor
from entidade.ator import Ator
from exceptions.filmeInexistenteException import FilmeInexistenteException
from DAOs.filme_dao import FilmeDAO
import time

def current_milli_time():
  return round(time.time() * 10)

def cria_id():
  return str(current_milli_time() - 17481983713)


class ControladorFilme():

  def __init__(self, controlador_sistema):
    self.__filme_DAO = FilmeDAO()
    self.__tela_filme = TelaFilme()
    self.__controlador_sistema = controlador_sistema

  @property
  def filmes(self):
    return self.__filme_DAO.get_all()

  def pega_filme_por_nome(self, titulo: str):
    for filme in self.__filme_DAO.get_all():
      if (filme.titulo == titulo):
        return filme
    raise FilmeInexistenteException(titulo)

  def incluir_filme(self):
    titulo = self.__tela_filme.pega_titulo_filme()

    diretor = None
    while diretor is None:
        diretor = self.__controlador_sistema.controlador_diretor.incluir_diretor(cria_id())
        if diretor is None:
            self.__tela_filme.mostra_mensagem("Tente novamente inserir os dados do diretor.")
    
    ator = None
    while ator is None:
        ator = self.__controlador_sistema.controlador_ator.incluir_ator("M", cria_id())
        if ator is None:
            self.__tela_filme.mostra_mensagem("Tente novamente inserir os dados do ator.")
    
    atriz = None
    while atriz is None:
        atriz = self.__controlador_sistema.controlador_ator.incluir_ator("F", cria_id())
        if atriz is None:
            self.__tela_filme.mostra_mensagem("Tente novamente inserir os dados da atriz.")
    
    if diretor is not None and ator is not None and atriz is not None:
        filme = Filme(titulo, diretor, ator, atriz)
        self.__filme_DAO.add(filme)
        self.__tela_filme.mostra_mensagem("Filme cadastrado com sucesso!")
    else:
        self.__tela_filme.mostra_mensagem("Erro: Não foi possível criar o filme devido a dados inválidos.")

  def lista_filmes(self):
    for f in self.__filme_DAO.get_all():
      categorias = []
      for categoria in f.categorias:
        categorias.append(categoria.nome)
      self.__tela_filme.mostra_filme({"titulo": f.titulo,
                                      "ator": f.ator_principal,
                                      "atriz": f.atriz_principal,
                                      "diretor": f.diretor,
                                      "categorias": categorias})

  def excluir_filme(self):
    try:
        self.lista_filmes()
        titulo_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_nome(titulo_filme)
        
        ator = filme.ator_principal
        atriz = filme.atriz_principal
        diretor = filme.diretor
        
        self.__controlador_sistema.controlador_ator.excluir_ator_por_id(ator.id)
        self.__controlador_sistema.controlador_ator.excluir_ator_por_id(atriz.id)
        self.__controlador_sistema.controlador_diretor.excluir_diretor_por_id(diretor.id)
        
        self.__filme_DAO.remove(filme.titulo)
        self.lista_filmes()
        
    except FilmeInexistenteException as e:
        self.__tela_filme.mostra_mensagem(f"ATENÇÃO: {e}")
  
  def alterar_titulo(self):
    try:
        self.lista_filmes()
        titulo_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_nome(titulo_filme)
        titulo = self.__tela_filme.pega_titulo_filme()
        filme.troca_titulo(titulo)
        self.__filme_DAO.update(filme)
        
    except FilmeInexistenteException as e:
        self.__tela_filme.mostra_mensagem(f"ATENÇÃO: {e}")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_filme, 2: self.lista_filmes, 3: self.excluir_filme, 4: self.alterar_titulo, 0: self.retornar}
    
    continua = True
    while continua:
      lista_opcoes[self.__tela_filme.tela_opcoes()]()
  
  def retorna_filme(self, titulo_do_filme):
    for filme in self.__filme_DAO.get_all():
      if filme.titulo == titulo_do_filme:
        return filme
    raise FilmeInexistenteException(titulo_do_filme)

  def inclui_categoria(self, filme, categoria):
    for f in self.__filme_DAO.get_all():
      if f.titulo == filme and categoria not in f.categorias:
        f.adiciona_categoria(categoria)
        self.__filme_DAO.update(f)
