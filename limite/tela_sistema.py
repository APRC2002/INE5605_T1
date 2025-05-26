class TelaSistema:
    
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
    
    def tela_opcoes(self):
        print("-------- Premiação de filmes nacionais que não premia atores ---------")
        print("Escolha sua opcao")
        print("1 - Membros Academia")
        print("2 - Atores")
        print("3 - Diretores")
        print("4 - Filmes")
        print("5 - Categorias")
        print("6 - Votação")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha uma opção:", [0, 1, 2, 3, 4, 5, 6])
        return opcao
