class IdRepetidoException(Exception):
    def __init__(self, id):
        self.mensagem = 'O ID "{}" já existe.'
        super().__init__(self.mensagem.format(id))
