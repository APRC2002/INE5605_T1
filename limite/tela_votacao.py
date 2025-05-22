
class TelaVotacao():
  def tela_opcoes(self):
    print("-------- VOTACAO  ----------")
    print("Escolha a opcao")
    print("1 - Incluir Voto")
    print("2 - Listar Votos")
    print("3 - Excluir Voto")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_voto(self):
    print("-------- DADOS DO VOTO ----------")
    id_membro = input("ID do votante: ")
    nome_categoria = input("Nome da Categoria: ")
    votado = input("Vencedor: ")
    return {"id": id_membro, "nome": nome_categoria, "votado": votado}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_voto(self, dados_voto):
    print("\n-------- DETALHES DO VOTO ----------")
    #print(f"ID DO VOTO: {dados_voto['id']}")
    print(f"MEMBRO: {dados_voto['votante']}")
    print(f"CATEGORIA: {dados_voto['categoria']}")
    print(f"VENCEDOR: {dados_voto["votado"]}")
    print("\n")

  #BLZ
  def seleciona_voto(self):
    id_voto = input("TID do votante: ")
    return id_voto
  #BLZ
  def mostra_mensagem(self, msg):
    print(msg)
