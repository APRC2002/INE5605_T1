class TelaAtor():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ATOR ----------")
    print("Escolha a opcao")
    print("1 - Alterar Ator")
    print("2 - Listar Atores")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_ator(self, genero_esperado):
    print("")
    if genero_esperado == "M":
      print("-------- DADOS ATOR ----------")
      id = input("id: ")
      nome = input("nome: ")
      data_de_nascimento = input("data de nascimento: ")
      nacionalidade = input("nacionalidade: ")
      genero = "M"
    elif genero_esperado == "F":
      print("-------- DADOS ATRIZ ----------")
      id = input("id: ")
      nome = input("nome: ")
      data_de_nascimento = input("data de nascimento: ")
      nacionalidade = input("nacionalidade: ")
      genero = "F"

    return {"id": id, "nome": nome, "data_de_nascimento": data_de_nascimento, "nacionalidade": nacionalidade, "genero": genero}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_ator(self, dados_ator):
    print("ID DO ATOR: ", dados_ator["id"])
    print("NOME DO ATOR: ", dados_ator["nome"])
    print("DATA DE NASCIMENTO DO ATOR: ", dados_ator["data_de_nascimento"])
    print("NACIONALIDADE DO ATOR: ", dados_ator["nacionalidade"])
    print("GENERO DO ATOR: ", dados_ator["genero"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_ator(self):
    id = input("Id do ator que deseja selecionar: ")
    return id

  def mostra_mensagem(self, msg):
    print(msg)
