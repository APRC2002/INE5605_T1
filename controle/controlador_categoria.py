from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria
from DAOs.categoria_dao import CategoriaDAO


class ControladorCategoria():

  def __init__(self, controlador_sistema):
    self.__categoria_DAO = CategoriaDAO()
    if len(self.__categoria_DAO.get_all()) == 0:
        categoria = Categoria("Melhor filme")
        self.__categoria_DAO.add(categoria)
    self.__controlador_sistema = controlador_sistema
    self.__tela_categoria = TelaCategoria()

  @property
  def categorias(self):
    return self.__categoria_DAO.get_all()

  def pega_categoria(self, nome: str):
    for categoria in self.__categoria_DAO.get_all():
      if(categoria.nome == nome):
        return categoria
    return None

  def incluir_categoria(self):
    nome_categoria = self.__tela_categoria.pega_nome()
    categoria = None
    for c in self.__categoria_DAO.get_all():
      if c.nome == nome_categoria:
        categoria = c
    if categoria == None:
      categoria = Categoria(nome_categoria)
      self.__categoria_DAO.add(categoria)
    else:
      self.__tela_categoria.mostra_mensagem("AVISO: Já há uma categoria cadastrada com esse nome")

  def alterar_nome_categoria(self):
    self.listar_categorias()
    categoria = self.__tela_categoria.pega_nome()
    novo_nome = self.__tela_categoria.pega_nome()
    for c in self.__categoria_DAO.get_all():
      if c.nome == categoria:
        c.nome = novo_nome
        self.__categoria_DAO.update(c)

  def adicionar_indicados(self):
    self.listar_categorias()
    nome_categoria = self.__tela_categoria.pega_nome()
    for c in self.__categoria_DAO.get_all():
      if c.nome == nome_categoria:
        categoria = c

    if len(categoria.indicados) < 5:
      self.__controlador_sistema.controlador_filme.lista_filmes()
      titulo_indicado = self.__tela_categoria.pega_indicado()
      indicado = self.__controlador_sistema.controlador_filme.retorna_filme(titulo_indicado)
      if indicado not in categoria.indicados:
        categoria.inclui_indicado(indicado)
        self.__controlador_sistema.controlador_filme.inclui_categoria(titulo_indicado, categoria)
        self.__categoria_DAO.update(categoria)
      else:
        self.__tela_categoria.mostra_mensagem("AVISO: Esse filme já foi indicado")
    else:
      self.__tela_categoria.mostra_mensagem("AVISO: Esta categoria já possui o número máximo de indicados")

  def remover_indicado(self):
    self.listar_categorias()
    nome_categoria = self.__tela_categoria.pega_nome()
    for c in self.__categoria_DAO.get_all():
      if c.nome == nome_categoria:
        categoria = c

    self.__tela_categoria.mostra_mensagem(f"Os indicados da categoria {categoria.nome} são {categoria.indicados}")
    indicado = self.__tela_categoria.pega_indicado()
    for i in categoria.indicados:
      if i.titulo == indicado:
        categoria.indicados.remove(i)
        self.__categoria_DAO.update(categoria)

  def listar_categorias(self):
    self.__tela_categoria.mostra_mensagem("----------------CATEGORIAS CADASTRADAS----------------")
    if len(self.__categoria_DAO.get_all()) == 0:
      self.__tela_categoria.mostra_mensagem("")
      self.__tela_categoria.mostra_mensagem("AVISO: Não há categorias cadastradas")
      self.__tela_categoria.mostra_mensagem("")
    else:
      for c in self.__categoria_DAO.get_all():
        indicados = []
        for indicado in c.indicados:
          indicados.append(indicado.titulo)
        self.__tela_categoria.mostra_categoria({"nome": c.nome, "indicados": indicados})
    self.__tela_categoria.mostra_mensagem("------------------------------------------------------")
    self.__tela_categoria.mostra_mensagem("")

  def excluir_categoria(self):
    self.listar_categorias()
    categoria = self.__tela_categoria.pega_nome()
    categoria = self.pega_categoria(categoria)
    if categoria is not None:
      self.__categoria_DAO.remove(categoria.nome)
    else:
      self.__tela_categoria.mostra_mensagem("Categoria não cadastrada")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_categoria, 2: self.alterar_nome_categoria, 3: self.adicionar_indicados, 4: self.remover_indicado, 5: self.listar_categorias, 6: self.excluir_categoria, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_categoria.tela_opcoes()]()
