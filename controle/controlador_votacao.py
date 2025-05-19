from limite.tela_votacao import TelaVotacao
from entidade.voto import Voto


class ControladorVotacao():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__votos = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_votacao = TelaVotacao()
    

  def incluir_voto(self):
    self.__controlador_sistema.controlador_membroAcademia.lista_membros()
    self.__controlador_sistema.controlador_categorias.lista_categorias()
    dados_voto = self.__tela_votacao.pega_dados_voto()

    membros_Academia = self.__controlador_sistema.controlador_membrosAcademia.pega_membro_por_id(dados_voto["id"])
    categorias = self.__controlador_sistema.controlador_categorias.pega_categoria_por_nome(dados_voto["nome"])
    if (membro_Academia is not None and categoria is not None):
      voto = Voto(membro_academia, categoria)
      self.__votos.append(voto)
    else:
      self.__tela_votacao.mostra_mensagem("ATENCAO: Voto já existente")

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

  def excluir_ator(self):
    self.lista_atores()
    id_ator = self.__tela_ator.seleciona_ator()
    ator = self.pega_ator_por_id(id_ator)

    if(ator is not None):
      self.__atores.remove(ator)
      self.lista_atores()
    else:
      self.__tela_ator.mostra_mensagem("ATENCAO: Ator não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_voto, 2: self.altera_voto, 3: self.lista_voto, 4: self.exclui_voto, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_votacao.tela_opcoes()]()
