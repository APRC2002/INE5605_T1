from limite.tela_votacao import TelaVotacao
from entidade.voto import Voto
from exceptions.filmeInexistenteException import FilmeInexistenteException
from DAOs.voto_dao import VotoDAO


class ControladorVotacao():

  def __init__(self, controlador_sistema):
    self.__voto_DAO = VotoDAO()
    self.__controlador_sistema = controlador_sistema
    self.__tela_votacao = TelaVotacao()
    

  def incluir_voto(self):
    try:
        self.__controlador_sistema.controlador_membroAcademia.lista_membrosAcademia()
        self.__controlador_sistema.controlador_categoria.listar_categorias()
        dados_voto = self.__tela_votacao.pega_dados_voto()

        membro_academia = self.__controlador_sistema.controlador_membroAcademia.pega_membro_por_id(dados_voto["id"])
        categoria = self.__controlador_sistema.controlador_categoria.pega_categoria(dados_voto["nome"])
        votado = self.__controlador_sistema.controlador_filme.pega_filme_por_nome(dados_voto["votado"])
        voto_repetido = False
        for v in self.__voto_DAO.get_all():
          if v.categoria == categoria and v.votante == membro_academia:
            voto_repetido = True
        if (membro_academia is not None and categoria is not None and not voto_repetido):
          if categoria in votado.categorias:
            voto = Voto(membro_academia, categoria, votado)
            self.__voto_DAO.add(voto)
        else:
          self.__tela_votacao.mostra_mensagem("ATENCAO: Voto já existente")
          
    except FilmeInexistenteException as e:
        self.__tela_votacao.mostra_mensagem(f"ATENÇÃO: {e}")

  def lista_votos(self):
    for voto in self.__voto_DAO.get_all():
      self.__tela_votacao.mostra_voto({"votante": voto.votante.nome, "categoria": voto.categoria.nome, "votado": voto.votado.titulo})

  def excluir_voto(self):
    self.lista_votos()
    id_voto = self.__tela_votacao.seleciona_voto()
    voto = self.pega_voto_por_id(id_voto)

    if(voto is not None):
      key = f"{voto.votante.id}_{voto.categoria.nome}"
      self.__voto_DAO.remove(key)
      self.lista_votos()
    else:
      self.__tela_votacao.mostra_mensagem("ATENCAO: Voto não existente")

  def mostra_vencedor_por_categoria(self):
    dict = {}
    self.__controlador_sistema.controlador_categoria.listar_categorias()
    categoria_escolhida = self.__tela_votacao.pega_categoria()
    for categoria in self.__controlador_sistema.controlador_categoria.categorias:
      if categoria.nome == categoria_escolhida:
        categoria_escolhida = categoria
    
    for indicado in categoria_escolhida.indicados:
      dict[indicado.titulo] = 0
      for voto in self.__voto_DAO.get_all():
        if voto.categoria == categoria_escolhida and voto.votado == indicado:
          dict[indicado.titulo] += 1
    
    vencedor = ''
    num_votos_vencedor = 0
    for filme in dict:
      if dict[filme] > num_votos_vencedor:
        vencedor = filme
        num_votos_vencedor = dict[filme]
    self.__tela_votacao.mostra_mensagem("----------VENCEDOR----------")
    self.__tela_votacao.mostra_mensagem(f"Vencedor: {vencedor}")
    self.__tela_votacao.mostra_mensagem("")

  def mostra_top_3_filmes_vencedores(self):
    filmes_wins = {}
    
    for categoria in self.__controlador_sistema.controlador_categoria.categorias:
      dict_votos = {}
      for indicado in categoria.indicados:
        dict_votos[indicado.titulo] = 0
        for voto in self.__voto_DAO.get_all():
          if voto.categoria == categoria and voto.votado == indicado:
            dict_votos[indicado.titulo] += 1
      
      vencedor_categoria = ''
      num_votos_vencedor = 0
      for filme in dict_votos:
        if dict_votos[filme] > num_votos_vencedor:
          vencedor_categoria = filme
          num_votos_vencedor = dict_votos[filme]
      
      if vencedor_categoria != '':
        if vencedor_categoria in filmes_wins:
          filmes_wins[vencedor_categoria] += 1
        else:
          filmes_wins[vencedor_categoria] = 1
    
    filmes_ordenados = sorted(filmes_wins.items(), key=lambda x: x[1], reverse=True)
    
    self.__tela_votacao.mostra_mensagem("----------TOP 3 FILMES VENCEDORES----------")
    if len(filmes_ordenados) == 0:
      self.__tela_votacao.mostra_mensagem("Não há filmes vencedores ainda")
    else:
      for i, (filme, wins) in enumerate(filmes_ordenados[:3], 1):
        self.__tela_votacao.mostra_mensagem(f"{i}º Lugar: {filme} - {wins} categoria(s)")
    self.__tela_votacao.mostra_mensagem("")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_voto, 2: self.lista_votos, 3: self.excluir_voto, 4: self.mostra_vencedor_por_categoria, 5: self.mostra_top_3_filmes_vencedores, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_votacao.tela_opcoes()]()
