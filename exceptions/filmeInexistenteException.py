class FilmeInexistenteException(Exception):
    def __init__(self, filme):
        self.mensagem = 'O filme "{}" não existe.'
        super().__init__(self.mensagem.format(filme))