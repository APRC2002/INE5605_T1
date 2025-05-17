from limite.tela_ator import TelaAtor
from entidade.ator import Ator

class ControladorAtor():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__atores = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_ator = TelaAtor()

  def pega_ator_por_id(self, id: int):
    for ator in self.__atores:
      if(ator.id == id):
        return ator
    return None

  def incluir_ator(self):
    dados_ator = self.__tela_ator.pega_dados_ator()
    l = self.pega_ator_por_id(dados_ator["id"])
    if l is None:
      ator = Ator(dados_ator["nome"], dados_ator["id"], dados_ator["data_de_nascimento"], dados_ator["nacionalidade"], dados_ator["genero"])
      self.__atores.append(ator)
    else:
      self.__tela_ator.mostra_mensagem("ATENCAO: Ator já existente")

  def alterar_ator(self):
    self.lista_ator()
    id_ator = self.__tela_livro.seleciona_ator()
    ator = self.pega_ator_por_id(id_ator)

    if(ator is not None):
      novos_dados_ator = self.__tela_ator.pega_dados_ator()
      ator.nome = novos_dados_ator["nome"]
      ator.id = novos_dados_ator["id"]
      ator.data_de_nascimento = novos_dados_ator["data_de_nascimento"]
      ator.nacionalidade = novos_dados_ator["nacionalidade"]
      ator.genero = novos_dados_ator["genero"]
      self.lista_ator()
    else:
      self.__tela_ator.mostra_mensagem("ATENCAO: Ator não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_ator(self):
    for ator in self.__atores:
      self.__tela_ator.mostra_ator({"titulo": livro.titulo, "codigo": livro.codigo})

  def excluir_livro(self):
    self.lista_livro()
    codigo_livro = self.__tela_livro.seleciona_livro()
    livro = self.pega_livro_por_codigo(codigo_livro)

    if(livro is not None):
      self.__livros.remove(livro)
      self.lista_livro()
    else:
      self.__tela_livro.mostra_mensagem("ATENCAO: Livro não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_livro, 2: self.alterar_livro, 3: self.lista_livro, 4: self.excluir_livro, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_livro.tela_opcoes()]()
