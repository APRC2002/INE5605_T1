import PySimpleGUI as sg

class TelaCategoria():
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
        elif values['5']:
            opcao = 5
        elif values['6']:
            opcao = 6
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- CATEGORIAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Categoria', "RD1", key='1')],
            [sg.Radio('Alterar Nome', "RD1", key='2')],
            [sg.Radio('Adicionar Indicados', "RD1", key='3')],
            [sg.Radio('Remover Indicados', "RD1", key='4')],
            [sg.Radio('Listar Categorias', "RD1", key='5')],
            [sg.Radio('Excluir Categoria', "RD1", key='6')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Categorias').Layout(layout)

    def pega_nome(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- NOME DA CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Nome da Categoria').Layout(layout)

        button, values = self.open()
        nome = values['nome']

        self.close()
        return nome

    def pega_indicado(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- INDICADO NA CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Indicado:', size=(15, 1)), sg.InputText('', key='indicado')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Indicado na Categoria').Layout(layout)

        button, values = self.open()
        indicado = values['indicado']

        self.close()
        return indicado

    def mostra_categoria(self, dados_categoria):
        string_categoria = ""
        for dado in dados_categoria:
            string_categoria = string_categoria + "NOME DA CATEGORIA: " + dados_categoria["nome"] + '\n'
            string_categoria = string_categoria + "INDICADOS DA CATEGORIA: " + str(dados_categoria["indicados"]) + '\n\n'

        sg.Popup('-------- DADOS DA CATEGORIA ----------', string_categoria)

    def seleciona_categoria(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CATEGORIA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o nome da categoria que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona categoria').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
