
class TelaCategoria():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CATEGORIAS  ----------")
    print("Escolha a opcao")
    print("1 - Incluir Categoria")
    print("2 - Alterar Nome")
    print("3 - Adicionar Indicados")
    print("4 - Remover Indicados")
    print("5 - Listar Categorias")
    print("6 - Excluir Categoria")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha uma opção:", [0, 1, 2, 3, 4, 5, 6])
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
  def pega_nome(self):
    #print("")
    print("-------- NOME DA CATEGORIA ----------")
    nome = input("Nome: ")
    print("")
    return nome

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_indicado(self):
    print("-------- INDICADO NA CATEGORIA ----------")
    indicado = input("Indicado: ")

    return indicado

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_categoria(self, dados_categoria):
    print("")
    print("NOME DA CATEGORIA: ", dados_categoria["nome"])
    print("INDICADOS DA CATEGORIA: ", dados_categoria["indicados"])
    print("")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_categoria(self):
    nome = input("Nome da categoria que deseja selecionar: ")
    return nome

  def mostra_mensagem(self, msg):
    print(msg)
