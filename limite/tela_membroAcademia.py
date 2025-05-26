
class TelaMembroAcademia():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ACADEMIA ----------")
    print("Escolha a opcao")
    print("1 - Incluir Membro")
    print("2 - Alterar Membro")
    print("3 - Listar Membros")
    print("4 - Excluir Membro")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha uma opção:", [0, 1, 2, 3, 4])
    print("")
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

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_membroAcademia(self):
    print("-------- DADOS MEMBROS ACADEMIA ----------")
    nome = input("Nome: ")
    nacionalidade = input("Nacionalidade: ")
    data_de_nascimento = input("Data de nascimento: ")
    print('')

    return {"nome": nome, "nacionalidade": nacionalidade, "data_de_nascimento": data_de_nascimento}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_membroAcademia(self, dados_membroAcademia):
    print("NOME DO MEMBRO: ", dados_membroAcademia["nome"])
    print("ID DO MEMBRO: ", dados_membroAcademia["ID"])
    print("NACIONALIDADE DO MEMBRO: ", dados_membroAcademia["nacionalidade"])
    print("DATA DE NASCIMENTO DO MEMBRO: ", dados_membroAcademia["data_de_nascimento"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_membroAcademia(self):
    id = input("ID do membro que deseja selecionar: ")
    return id

  def mostra_mensagem(self, msg):
    print(msg)
    print('')