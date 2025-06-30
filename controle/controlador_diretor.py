from limite.tela_diretor import TelaDiretor
from entidade.diretor import Diretor
from exceptions.stringInvalida import NomeVazioException
from DAOs.diretor_dao import DiretorDAO


class ControladorDiretor():

  def __init__(self, controlador_sistema):
    self.__diretor_DAO = DiretorDAO()
    self.__controlador_sistema = controlador_sistema
    self.__tela_diretor = TelaDiretor()

  @property
  def diretores(self):
    return self.__diretor_DAO.get_all()
  
  def pega_diretor_por_id(self, id: int):
    for diretor in self.__diretor_DAO.get_all():
      if(diretor.id == id):
        return diretor
    return None

  def incluir_diretor(self, id):
    try:
        dados_diretor = self.__tela_diretor.pega_dados_diretor()
        
        if not dados_diretor["nome"].strip():
            raise NomeVazioException(dados_diretor["nome"])
        
        diretor_existente = self.pega_diretor_por_id(id)
        if diretor_existente is not None:
            self.__tela_diretor.mostra_mensagem("ATENÇÃO: Diretor já existente")
            return None
        
        novo_diretor = Diretor(
            id,
            dados_diretor["nome"],
            dados_diretor["data_de_nascimento"],
            dados_diretor["nacionalidade"]
        )
        self.__diretor_DAO.add(novo_diretor)
        self.__tela_diretor.mostra_mensagem("Diretor cadastrado com sucesso!")
        return novo_diretor
        
    except NomeVazioException as e:
        self.__tela_diretor.mostra_mensagem(f"ERRO: {e}")
        return None
    except Exception as e:
        self.__tela_diretor.mostra_mensagem(f"Erro inesperado: {e}")
        return None
  def alterar_diretor(self):
    try:
        self.lista_diretores()
        id_diretor = self.__tela_diretor.seleciona_diretor()
        try:
            id_diretor = int(id_diretor)
            diretor = self.pega_diretor_por_id(id_diretor)

            if diretor is None:
                self.__tela_diretor.mostra_mensagem("ATENÇÃO: Diretor não encontrado.")
                return

            novos_dados_diretor = self.__tela_diretor.pega_dados_diretor()
            
            if not novos_dados_diretor["nome"].strip():
                raise NomeVazioException(novos_dados_diretor["nome"])

            diretor.nome = novos_dados_diretor["nome"]
            diretor.data_de_nascimento = novos_dados_diretor["data_de_nascimento"]
            diretor.nacionalidade = novos_dados_diretor["nacionalidade"]

            self.__diretor_DAO.update(diretor)
            self.lista_diretores()
            self.__tela_diretor.mostra_mensagem("Diretor atualizado com sucesso!")
        except ValueError:
            self.__tela_diretor.mostra_mensagem("ATENÇÃO: ID inválido. Digite um número.")

    except NomeVazioException as e:
        self.__tela_diretor.mostra_mensagem(f"ERRO: {e}")
    except Exception as e:
        self.__tela_diretor.mostra_mensagem(f"Erro inesperado: {e}")


  def lista_diretores(self):
    dados_diretor = []
    for diretor in self.__diretor_DAO.get_all():
      dados_diretor.append({"id": diretor.id, "nome": diretor.nome, "data_de_nascimento": diretor.data_de_nascimento, "nacionalidade": diretor.nacionalidade})
    self.__tela_diretor.mostra_diretor(dados_diretor)

  def excluir_diretor(self):
    self.lista_diretores()
    id_diretor = self.__tela_diretor.seleciona_diretor()
    try:
        id_diretor = int(id_diretor)
        diretor = self.pega_diretor_por_id(id_diretor)

        if(diretor is not None):
          self.__diretor_DAO.remove(diretor.id)
          self.lista_diretores()
        else:
          self.__tela_diretor.mostra_mensagem("ATENCAO: Diretor não existente")
    except ValueError:
        self.__tela_diretor.mostra_mensagem("ATENÇÃO: ID inválido. Digite um número.")

  def excluir_diretor_por_id(self, id):
    diretor = self.pega_diretor_por_id(id)
    if diretor is not None:
        self.__diretor_DAO.remove(diretor.id)
  
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.alterar_diretor, 2: self.lista_diretores, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_diretor.tela_opcoes()]()
