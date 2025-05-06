class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Oscars ---------")
        print("Escolha sua opcao")
        print("1 - Membros Academia")
        print("2 - Atores")
        print("3 - Diretores")
        print("4 - Filmes")
        print("5 - Categorias")
        print("6 - Votação")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    