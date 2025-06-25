class entradaInvalida(Exception):
    def __init__(self, entrada):
        self.mensagem = 'A entrada "{}" não é válida.'
        super().__init__(self.mensagem.format(entrada))