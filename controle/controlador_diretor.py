from limite.tela_diretor import TelaDiretor
from entidade.diretor import Diretor

class ControladorDiretor():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__diretores = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_diretor = TelaDiretor()

  def pega_diretor_por_id(self, id: int):
    for diretor in self.__diretores:
      if(diretor.id == id):
        return diretor
    return None

  def incluir_diretor(self):
    dados_diretor = self.__tela_diretor.pega_dados_diretor()
    l = self.pega_diretor_por_id(dados_diretor["id"])
    if l is None:
      diretor = Diretor(dados_diretor["id"], dados_diretor["nome"], dados_diretor["data_de_nascimento"], dados_diretor["nacionalidade"])
      self.__diretores.append(diretor)
      return diretor
    else:
      self.__tela_diretor.mostra_mensagem("ATENCAO: Diretor já existente")

  def alterar_diretor(self):
    self.lista_diretores()
    id_diretor = self.__tela_diretor.seleciona_diretor()
    diretor = self.pega_diretor_por_id(id_diretor)

    if(diretor is not None):
      novos_dados_diretor = self.__tela_diretor.pega_dados_diretor()
      diretor.id = novos_dados_diretor["id"]
      diretor.nome = novos_dados_diretor["nome"]
      diretor.data_de_nascimento = novos_dados_diretor["data_de_nascimento"]
      diretor.nacionalidade = novos_dados_diretor["nacionalidade"]
      self.lista_diretores()
    else:
      self.__tela_diretor.mostra_mensagem("ATENCAO: Diretor não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_diretores(self):
    for diretor in self.__diretores:
      self.__tela_diretor.mostra_diretor({"id": diretor.id, "nome": diretor.nome, "data_de_nascimento": diretor.data_de_nascimento, "nacionalidade": diretor.nacionalidade})
    if len(self.__diretores) == 0:
      print("Não há diretores cadastrados")

  def excluir_diretor(self):
    self.lista_diretores()
    id_diretor = self.__tela_diretor.seleciona_diretor()
    diretor = self.pega_diretor_por_id(id_diretor)

    if(diretor is not None):
      self.__diretores.remove(diretor)
      self.lista_diretores()
    else:
      self.__tela_diretor.mostra_mensagem("ATENCAO: Diretor não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.alterar_diretor, 2: self.lista_diretores, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_diretor.tela_opcoes()]()
