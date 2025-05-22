
from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria


class ControladorCategoria():

  def __init__(self, controlador_sistema):
    self.__categorias = []
    categoria = Categoria("Melhor filme")
    self.__categorias.append(categoria)
    self.__controlador_sistema = controlador_sistema
    self.__tela_categoria = TelaCategoria()

  def pega_categoria(self, nome: str):
    for categoria in self.__categorias:
      if(categoria.nome == nome):
        return categoria
    return None

  # Sugestão: não deixe cadastrar duas categorias com o mesmo nome
  def incluir_categoria(self):
    nome_categoria = self.__tela_categoria.pega_nome()
    categoria = Categoria(nome_categoria)
    self.__categorias.append(categoria)

  def alterar_nome_categoria(self):
    self.listar_categorias()
    categoria = self.__tela_categoria.pega_nome()
    novo_nome = self.__tela_categoria.pega_nome()
    for c in self.__categorias:
      if c.nome == categoria:
        c.nome = novo_nome

  def adicionar_indicados(self):
    self.listar_categorias()
    nome_categoria = self.__tela_categoria.pega_nome()
    for c in self.__categorias:
      if c.nome == nome_categoria:
        categoria = c
    self.__controlador_sistema.controlador_filme.lista_filmes()
    titulo_indicado = self.__tela_categoria.pega_indicado()
    indicado = self.__controlador_sistema.controlador_filme.retorna_filme(titulo_indicado)
    categoria.inclui_indicado(indicado)
    self.__controlador_sistema.controlador_filme.inclui_categoria(titulo_indicado, categoria)

  def remover_indicado(self):
    pass

  def listar_categorias(self):
    for c in self.__categorias:
      indicados = []
      for indicado in c.indicados:
        indicados.append(indicado.titulo)
      self.__tela_categoria.mostra_categoria({"nome": c.nome, "indicados": indicados})

  def excluir_categoria(self):
    pass

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_categoria, 2: self.alterar_nome_categoria, 3: self.adicionar_indicados, 4: self.remover_indicado, 5: self.listar_categorias, 7: self.excluir_categoria, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_categoria.tela_opcoes()]()

"""







  def alterar_categoria(self):
    self.lista_categorias()
    nome_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria(nome_categoria)

    if(categoria is not None):
      novo_nome = self.__tela_categoria.pega_nome()
      categoria.nome = novo_nome
      self.lista_categorias()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  def adicionar_indicados(self):
    self.lista_categorias()
    nome_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria(nome_categoria)

    if(categoria is not None):
      novos_indicados = self.__tela_categoria.pega_indicados().split(",")
      for indicado in novos_indicados:
        categoria.inclui_indicados(indicado)
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  def remover_indicados(self):
    self.lista_categorias()
    nome_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria(nome_categoria)

    if(categoria is not None):
      indicados_removidos = self.__tela_categoria.pega_indicados().split(",")
      categoria.remove_indicados(indicados_removidos)
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  def alterar_indicados(self):
    self.lista_categorias()
    nome_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria(nome_categoria)

    if(categoria is not None):
      novos_indicados = self.__tela_categoria.pega_indicados().split(",") # oque acontece com esse .split() se o input for de um candidato só?????????
      categoria.set_indicados(novos_indicados)
      self.lista_categorias()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_categorias(self):
    for categoria in self.__categorias:
      self.__tela_categoria.mostra_categoria({"nome": categoria.nome, "indicados": categoria.indicados})

  def excluir_categoria(self):
    self.lista_categorias()
    nome_categoria = self.__tela_categoria.seleciona_categoria()
    categoria = self.pega_categoria(nome_categoria)

    if(categoria is not None):
      self.__categorias.remove(categoria)
      self.lista_categorias()
    else:
      self.__tela_categoria.mostra_mensagem("ATENCAO: Categoria não existente")
"""
