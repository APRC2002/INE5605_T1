from limite.tela_membroAcademia import TelaMembroAcademia
from entidade.membroAcademia import MembroAcademia
from DAOs.membro_academia_dao import MembroAcademiaDAO
import time

def current_milli_time():
  return round(time.time() * 10)

def cria_id():
  return int(current_milli_time() - 17481983713)


class ControladorMembroAcademia():

  def __init__(self, controlador_sistema):
    self.__membro_academia_DAO = MembroAcademiaDAO()
    """
    # Add sample data if DAO is empty
    if len(self.__membro_academia_DAO.get_all()) == 0:
        membro = MembroAcademia("123", "Membro1", 123, "BR")
        self.__membro_academia_DAO.add(membro)
        membro = MembroAcademia("234", "Membro2", 123, "BR")
        self.__membro_academia_DAO.add(membro)
        membro = MembroAcademia("345", "Membro3", 123, "BR")
        self.__membro_academia_DAO.add(membro)
    """
    self.__tela_membroAcademia = TelaMembroAcademia()
    self.__controlador_sistema = controlador_sistema

  @property
  def membrosAcademia(self):
    return self.__membro_academia_DAO.get_all()

  def pega_membro_por_id(self, id: int):
    for membro in self.__membro_academia_DAO.get_all():
      if(str(membro.id) == str(id)):
        return membro
    return None

  def incluir_membroAcademia(self):
    dados_membroAcademia = self.__tela_membroAcademia.pega_dados_membroAcademia()
    membroAcademia = MembroAcademia(int(cria_id()), dados_membroAcademia["nome"], dados_membroAcademia["data_de_nascimento"], dados_membroAcademia["nacionalidade"])
    self.__membro_academia_DAO.add(membroAcademia)

  def alterar_membro(self):
    self.lista_membrosAcademia()
    id_membro = self.__tela_membroAcademia.seleciona_membroAcademia()
    try:
        id_membro = int(id_membro)
        membroAcademia = self.pega_membro_por_id(id_membro)

        if(membroAcademia is not None):
          novos_dados_membroAcademia = self.__tela_membroAcademia.pega_dados_membroAcademia()
          membroAcademia.nome = novos_dados_membroAcademia["nome"]
          membroAcademia.nacionalidade = novos_dados_membroAcademia["nacionalidade"]
          membroAcademia.data_de_nascimento = novos_dados_membroAcademia["data_de_nascimento"]
          self.__membro_academia_DAO.update(membroAcademia)
          self.lista_membrosAcademia()
        else:
          self.__tela_membroAcademia.mostra_mensagem("ATENCAO: Membro não existente")
    except ValueError:
        self.__tela_membroAcademia.mostra_mensagem("ATENCAO: ID inválido. Digite um número.")

  def lista_membrosAcademia(self):
    self.__tela_membroAcademia.mostra_mensagem("--------------MEMBROS DA ACADEMIA--------------")

    if len(self.__membro_academia_DAO.get_all()) == 0:
      self.__tela_membroAcademia.mostra_mensagem("Aviso: Não há membros cadastrados")
    for membro in self.__membro_academia_DAO.get_all():
      self.__tela_membroAcademia.mostra_membroAcademia({"nome": membro.nome, "ID": membro.id, "nacionalidade": membro.nacionalidade, "data_de_nascimento": membro.data_de_nascimento})

  def excluir_membro(self):
    self.lista_membrosAcademia()
    id_membroAcademia = self.__tela_membroAcademia.seleciona_membroAcademia()
    try:
        id_membroAcademia = int(id_membroAcademia)
        membroAcademia = self.pega_membro_por_id(id_membroAcademia)

        if(membroAcademia is not None):
          self.__membro_academia_DAO.remove(membroAcademia.id)
          self.lista_membrosAcademia()
        else:
          self.__tela_membroAcademia.mostra_mensagem("ATENCAO: Membro não existente")
    except ValueError:
        self.__tela_membroAcademia.mostra_mensagem("ATENCAO: ID inválido. Digite um número.")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_membroAcademia, 2: self.alterar_membro, 3: self.lista_membrosAcademia, 4: self.excluir_membro, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_membroAcademia.tela_opcoes()]()
