
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
    
    def set_indicados(self, indicados):
        self.__indicados = indicados # por algum caralaho de motivo redefinir_indicados não estava funcionando com o setter????????

    def inclui_indicados(self, indicados):
        self.__indicados.append(indicados)
    
    def remove_indicados(self, indicados):
        for indicado in indicados:
            self.__indicados.remove(indicado)