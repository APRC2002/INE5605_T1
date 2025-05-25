class TelaDiretor():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- DIRETOR ----------")
    print("Escolha a opcao")
    print("1 - Alterar Diretor")
    print("2 - Listar Diretor")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_diretor(self):
    print("")
    print("-------- DADOS DIRETOR ----------")
    nome = input("nome: ")
    data_de_nascimento = input("data de nascimento: ")
    nacionalidade = input("nacionalidade: ")
    

    return {"nome": nome, "data_de_nascimento": data_de_nascimento, "nacionalidade": nacionalidade}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_diretor(self, dados_diretor):
    print("ID DO DIRETORR: ", dados_diretor["id"])
    print("NOME DO DIRETOR: ", dados_diretor["nome"])
    print("DATA DE NASCIMENTO DO DIRETOR: ", dados_diretor["data_de_nascimento"])
    print("NACIONALIDADE DO DIRETOR: ", dados_diretor["nacionalidade"])
    print("\n")

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_diretor(self):
    id = input("Id do diretor que deseja selecionar: ")
    return id

  def mostra_mensagem(self, msg):
    print(msg)
