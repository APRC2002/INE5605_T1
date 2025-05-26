class NomeVazioException(Exception):
    def __init__(self, nome):
        self.mensagem = 'O nome "{}" não é valido pois está vazio.'
        super().__init__(self.mensagem.format(nome))