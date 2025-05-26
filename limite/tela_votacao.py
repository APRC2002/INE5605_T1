
class TelaVotacao():
  def tela_opcoes(self):
    print("-------- VOTACAO  ----------")
    print("Escolha a opcao")
    print("1 - Incluir Voto")
    print("2 - Listar Votos")
    print("3 - Excluir Voto")
    print("4 - Visualizar vencedores")
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

  def pega_categoria(self):
    print("---ESCOLHA A CATEGORIA---")
    categoria = input("Categoria: ")
    return categoria
  
  #BLZ
  def seleciona_voto(self):
    id_voto = input("TID do votante: ")
    return id_voto
  #BLZ
  def mostra_mensagem(self, msg):
    print(msg)
