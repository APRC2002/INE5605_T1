class TelaAtor():

  def tela_opcoes(self):
    print("-------- ATOR ----------")
    print("Escolha a opcao")
    print("1 - Alterar Ator")
    print("2 - Listar Atores")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha uma opção:", [0, 1, 2])
    return opcao

  def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor inválido!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

  def pega_dados_ator(self, genero_esperado):
    print("")
    if genero_esperado == "M":
      print("-------- DADOS ATOR ----------")
      nome = input("nome: ")
      data_de_nascimento = input("data de nascimento: ")
      nacionalidade = input("nacionalidade: ")
      genero = "M"
    elif genero_esperado == "F":
      print("-------- DADOS ATRIZ ----------")
      nome = input("nome: ")
      data_de_nascimento = input("data de nascimento: ")
      nacionalidade = input("nacionalidade: ")
      genero = "F"

    return {"nome": nome, "data_de_nascimento": data_de_nascimento, "nacionalidade": nacionalidade, "genero": genero}

  def mostra_ator(self, dados_ator):
    print("ID DO ATOR: ", dados_ator["id"])
    print("NOME DO ATOR: ", dados_ator["nome"])
    print("DATA DE NASCIMENTO DO ATOR: ", dados_ator["data_de_nascimento"])
    print("NACIONALIDADE DO ATOR: ", dados_ator["nacionalidade"])
    print("GENERO DO ATOR: ", dados_ator["genero"])
    print("\n")

  def seleciona_ator(self):
    id = input("Id do ator que deseja selecionar: ")
    return id

  def mostra_mensagem(self, msg):
    print(msg)
