class GeneroInvalidoException(Exception):
    def __init__(self, genero):
        self.mensagem = 'O genero {} é inválido. Gêneros válidos são "M" e "F".'
        super().__init__(self.mensagem.format(genero))