from limite.tela_votacao import TelaVotacao
from entidade.voto import Voto


class ControladorVotacao():

  # Fazer lançamento e tratamento de exceções, ao invés de apenas mostrar mensagem na tela.
  def __init__(self, controlador_sistema):
    self.__votos = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_votacao = TelaVotacao()
    

  def incluir_voto(self):
    self.__controlador_sistema.controlador_membroAcademia.lista_membrosAcademia()
    self.__controlador_sistema.controlador_categoria.listar_categorias()
    dados_voto = self.__tela_votacao.pega_dados_voto()

    membro_academia = self.__controlador_sistema.controlador_membroAcademia.pega_membro_por_id(dados_voto["id"])
    categoria = self.__controlador_sistema.controlador_categoria.pega_categoria(dados_voto["nome"])
    vencedor = self.__controlador_sistema.controlador_filme.pega_filme_por_nome(dados_voto["votado"])
    if (membro_academia is not None and categoria is not None):
      voto = Voto(membro_academia, categoria, vencedor)
      self.__votos.append(voto)
    else:
      self.__tela_votacao.mostra_mensagem("ATENCAO: Voto já existente")

  def alterar_voto(self):
    self.lista_votos()
    id_voto = self.__tela_votacao.seleciona_voto_por_id()
    voto_para_alterar = None
    for voto in self.__votos:
      if voto.id == id_voto:
        voto_para_alterar = voto
        break
    else:
        self.__tela_votacao.mostra_mensagem("ATENCAO: Voto não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_votos(self):
    for voto in self.__votos:
      self.__tela_votacao.mostra_voto({"votante": voto.votante.nome, "categoria": voto.categoria.nome, "votado": voto.vencedor.titulo})

  def excluir_voto(self):
    self.lista_votos()
    id_voto = self.__tela_votacao.seleciona_voto()
    voto = self.pega_voto_por_id(id_voto)

    if(voto is not None):
      self.__votos.remove(voto)
      self.lista_votos()
    else:
      self.__tela_votacao.mostra_mensagem("ATENCAO: Voto não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_voto, 2: self.alterar_voto, 3: self.lista_votos, 4: self.excluir_voto, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_votacao.tela_opcoes()]()
