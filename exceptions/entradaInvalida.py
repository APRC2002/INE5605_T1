class entradaInvalida(Exception):
    def __init__(self, entrada):
        self.mensagem = 'A entrada {} não é váliida'
        super().__init__(self.mensagem.format(entrada))