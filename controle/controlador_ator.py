from limite.tela_ator import TelaAtor
from entidade.ator import Ator

class ControladorAtor():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__atores = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_ator = TelaAtor()

  @property
  def atores(self):
    return self.__atores
  
  def pega_ator_por_id(self, id: int):
    for ator in self.__atores:
      if(ator.id == id):
        return ator
    return None

  def incluir_ator(self, genero):
    dados_ator = self.__tela_ator.pega_dados_ator(genero)
    a = self.pega_ator_por_id(dados_ator["id"])
    if a is None:
      ator = Ator(dados_ator["id"], dados_ator["nome"], dados_ator["data_de_nascimento"], dados_ator["nacionalidade"], dados_ator["genero"])
      self.__atores.append(ator)
      return ator
    else:
      self.__tela_ator.mostra_mensagem("ATENCAO: Ator já existente")

  def alterar_ator(self):
    self.lista_atores()
    id_ator = self.__tela_ator.seleciona_ator()
    ator = self.pega_ator_por_id(id_ator)

    if(ator is not None):
      novos_dados_ator = self.__tela_ator.pega_dados_ator()
      ator.nome = novos_dados_ator["nome"]
      ator.id = novos_dados_ator["id"]
      ator.data_de_nascimento = novos_dados_ator["data_de_nascimento"]
      ator.nacionalidade = novos_dados_ator["nacionalidade"]
      ator.genero = novos_dados_ator["genero"]
      self.lista_atores()
    else:
      self.__tela_ator.mostra_mensagem("ATENCAO: Ator não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_atores(self):
    for ator in self.__atores:
      self.__tela_ator.mostra_ator({"nome": ator.nome, "id": ator.id, "data_de_nascimento": ator.data_de_nascimento, "nacionalidade": ator.nacionalidade, "genero": ator.genero})
    if len(self.__atores) == 0:
      print("Não há atores cadastrados")

  def excluir_ator(self):
    self.lista_atores()
    id_ator = self.__tela_ator.seleciona_ator()
    ator = self.pega_ator_por_id(id_ator)

    if(ator is not None):
      self.__atores.remove(ator)
      self.lista_atores()
    else:
      self.__tela_ator.mostra_mensagem("ATENCAO: Ator não existente")
  
  def excluir_ator_por_id(self, id):
    ator = self.pega_ator_por_id(id)
    self.__atores.remove(ator)

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.alterar_ator, 2: self.lista_atores, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_ator.tela_opcoes()]()
