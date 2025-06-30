class Categoria:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__indicados = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def indicados(self):
        return self.__indicados
    
    @indicados.setter
    def indicados(self, indicados):
        self.__indicados = indicados

    def inclui_indicado(self, indicados):
        self.__indicados.append(indicados)
    
    def remove_indicado(self, indicados):
        for indicado in indicados:
            self.__indicados.remove(indicado)
    
    def __eq__(self, other):
        if isinstance(other, Categoria):
            return self.__nome == other.__nome
        return False
    
    def __hash__(self):
        return hash(self.__nome)
