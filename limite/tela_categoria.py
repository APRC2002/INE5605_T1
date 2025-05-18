
class TelaCategoria():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- CATEGORIAS  ----------")
    print("Escolha a opcao")
    print("1 - Incluir Categoria")
    print("2 - Alterar Nome")
    print("3 - Adicionar Indicados")
    print("4 - Remover Indicados")
    print("5 - Redefinir Indicados")
    print("6 - Listar Categorias")
    print("7 - Excluir Categoria")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_nome_categoria(self):                 # NO EXEMPLO ESSE MÉTODO ERA USADO PRA CRIAR UM OBJETO, PORTANTO PEGAVA 
    print("-------- DADOS CATEGORIA ----------") # TODOS OS DADOS NECESSÁRIOS. NESSE CASO, ELE PEGA SÓ O NOME POIS OS 
    nome = input("Nome: ")                       # INDICADOS SÃO INICIALIZADOS COMO UMA LISTA VAZIA
                                                 # OU TIRA ESSA REDUNDANCIA COM pega_nome OU RESOLVE O PROBLEMA DE INICIALIZAR 
    return nome                                  # JÁ COM OS INDICADOS

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_nome(self):
    print("-------- NOME DA CATEGORIA ----------")
    nome = input("Nome: ")

    return nome

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_indicados(self):
    print("-------- INDICADOS NA CATEGORIA ----------")
    indicados = input("Indicados: ")

    return indicados

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_categoria(self, dados_categoria):
    print("NOME DA CATEGORIA: ", dados_categoria["nome"])
    print("INDICADOS DA CATEGORIA: ", dados_categoria["indicados"])
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_categoria(self):
    nome = input("Nome da categoria que deseja selecionar: ")
    return nome

  def mostra_mensagem(self, msg):
    print(msg)
