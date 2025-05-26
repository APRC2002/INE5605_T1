
class TelaFilme():
  def tela_opcoes(self):
    print("-------- FILMES  ----------")
    print("Escolha a opcao")
    print("1 - Incluir Filme")
    print("2 - Listar Filmes")
    print("3 - Excluir Filme")
    print("4 - Alterar Título")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha uma opção:", [0, 1, 2, 3, 4])
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

  def pega_titulo_filme(self):
    print("")
    print("-------- TITULO DO FILME ----------")
    nome = input("Titulo: ")
    return nome

  def mostra_filme(self, dados_filme):
    print("TITULO DO FILME: ", dados_filme["titulo"])
    print("DIRETOR: ", dados_filme["diretor"].nome)
    print("ATOR PRINCIPAL: ", dados_filme["ator"].nome)
    print("ATRIZ PRINCIPAL: ", dados_filme["atriz"].nome)
    print("CATEGORIAS: ", dados_filme["categorias"])
    print("\n")

  def seleciona_filme(self):
    titulo = input("Titulo do filme que deseja selecionar: ")
    return titulo

  def mostra_mensagem(self, msg):
    print(msg)
