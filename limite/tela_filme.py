
class TelaFilme():
  def tela_opcoes(self):
    print("")
    print("-------- FILMES  ----------")
    print("Escolha a opcao")
    print("1 - Incluir Filme")
    print("2 - Listar Filmes")
    print("3 - Excluir Filme")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_titulo_filme(self):
    print("")
    print("-------- TITULO DO FILME ----------")
    nome = input("Titulo: ")
    return nome

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_filme(self, dados_filme):
    print("TITULO DO FILME: ", dados_filme["titulo"])
    print("DIRETOR: ", dados_filme["diretor"].nome)
    print("ATOR PRINCIPAL: ", dados_filme["ator"].nome)
    print("ATRIZ PRINCIPAL: ", dados_filme["atriz"].nome)
    print("CATEGORIAS: ", dados_filme["categorias"])
    print("\n")

  #BLZ
  def seleciona_filme(self):
    titulo = input("Titulo do filme que deseja selecionar: ")
    return titulo
  #BLZ
  def mostra_mensagem(self, msg):
    print(msg)
