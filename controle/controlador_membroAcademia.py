from limite.tela_membroAcademia import TelaMembroAcademia
from entidade.membroAcademia import MembroAcademia

class ControladorMembroAcademia():

  def __init__(self, controlador_sistema):
    self.__membrosAcademia = []
    self.__tela_membroAcademia = TelaMembroAcademia()
    self.__controlador_sistema = controlador_sistema

  def pega_membro_por_id(self, id: int):
    for membro in self.__membrosAcademia:
      if(membro.id == id):
        return membro
    return None

  # Sugestão: não deixe cadastrar dois membrosAcademia com o mesmo  ID
  def incluir_membroAcademia(self):
    dados_membroAcademia = self.__tela_membroAcademia.pega_dados_membroAcademia()
    membroAcademia = MembroAcademia(dados_membroAcademia["id"], dados_membroAcademia["nome"], dados_membroAcademia["data_de_nascimento"], dados_membroAcademia["nacionalidade"])
    self.__membrosAcademia.append(membroAcademia)

  def alterar_membro(self):
    self.lista_membrosAcademia()
    id_membro = self.__tela_membroAcademia.seleciona_membroAcademia()
    membroAcademia = self.pega_membro_por_id(id_membro)

    if(membroAcademia is not None):
      novos_dados_membroAcademia = self.__tela_membroAcademia.pega_dados_membroAcademia()
      membroAcademia.nome = novos_dados_membroAcademia["nome"]
      membroAcademia.nacionalidade = novos_dados_membroAcademia["nacionalidade"]
      membroAcademia.id = novos_dados_membroAcademia["id"]
      membroAcademia.data_de_nascimento = novos_dados_membroAcademia["data_de_nascimento"]
      self.lista_membrosAcademia()
    else:
      self.__tela_membroAcademia.mostra_mensagem("ATENCAO: Membro não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_membrosAcademia(self):
    for membro in self.__membrosAcademia:
      self.__tela_membroAcademia.mostra_membroAcademia({"nome": membro.nome, "ID": membro.id, "nacionalidade": membro.nacionalidade, "data_de_nascimento": membro.data_de_nascimento})

  def excluir_membro(self):
    self.lista_membrosAcademia()
    id_membroAcademia = self.__tela_membroAcademia.seleciona_membroAcademia()
    membroAcademia = self.pega_membro_por_id(id_membroAcademia)

    if(membroAcademia is not None):
      self.__membrosAcademia.remove(membroAcademia)
      self.lista_membrosAcademia()
    else:
      self.__tela_membroAcademia.mostra_mensagem("ATENCAO: Membro não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_membroAcademia, 2: self.alterar_membro, 3: self.lista_membros, 4: self.excluir_membro, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_membroAcademia.tela_opcoes()]()