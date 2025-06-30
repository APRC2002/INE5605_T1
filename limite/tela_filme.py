import PySimpleGUI as sg

class TelaFilme():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- FILMES ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Filme', "RD1", key='1')],
            [sg.Radio('Listar Filmes', "RD1", key='2')],
            [sg.Radio('Excluir Filme', "RD1", key='3')],
            [sg.Radio('Alterar Título', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Filmes').Layout(layout)

    def pega_titulo_filme(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- TÍTULO DO FILME ----------', font=("Helvica", 25))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Título do Filme').Layout(layout)

        button, values = self.open()
        titulo = values['titulo']

        self.close()
        return titulo

    def mostra_filme(self, dados_filme):
        string_filme = ""
        for filme in dados_filme:
            string_filme = string_filme + "TÍTULO DO FILME: " + filme["titulo"] + '\n'
            string_filme = string_filme + "DIRETOR: " + filme["diretor"].nome + '\n'
            string_filme = string_filme + "ATOR PRINCIPAL: " + filme["ator"].nome + '\n'
            string_filme = string_filme + "ATRIZ PRINCIPAL: " + filme["atriz"].nome + '\n'
            string_filme = string_filme + "CATEGORIAS: " + str(filme["categorias"]) + '\n\n'

        sg.Popup('-------- DADOS DO FILME ----------', string_filme)

    def seleciona_filme(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR FILME ----------', font=("Helvica", 25))],
            [sg.Text('Digite o título do filme que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Título:', size=(15, 1)), sg.InputText('', key='titulo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona filme').Layout(layout)

        button, values = self.open()
        titulo = values['titulo']
        self.close()
        return titulo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
