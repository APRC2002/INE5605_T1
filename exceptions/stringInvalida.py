class stringInvalida(Exception):
    def __init__(self, string):
        self.mensagem = 'A string {} não é váliida pois está vazia.'
        super().__init__(self.mensagem.format(string))