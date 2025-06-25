import PySimpleGUI as sg

class TelaDiretor():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- DIRETOR ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Alterar Diretor', "RD1", key='1')],
            [sg.Radio('Listar Diretores', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Diretores').Layout(layout)

    def pega_dados_diretor(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DIRETOR ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText('', key='data_de_nascimento')],
            [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Diretor').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        data_de_nascimento = values['data_de_nascimento']
        nacionalidade = values['nacionalidade']

        self.close()
        return {"nome": nome, "data_de_nascimento": data_de_nascimento, "nacionalidade": nacionalidade}

    def mostra_diretor(self, dados_diretor):
        string_diretor = ""
        string_diretor = string_diretor + "ID DO DIRETOR: " + str(dados_diretor["id"]) + '\n'
        string_diretor = string_diretor + "NOME DO DIRETOR: " + dados_diretor["nome"] + '\n'
        string_diretor = string_diretor + "DATA DE NASCIMENTO DO DIRETOR: " + dados_diretor["data_de_nascimento"] + '\n'
        string_diretor = string_diretor + "NACIONALIDADE DO DIRETOR: " + dados_diretor["nacionalidade"] + '\n\n'

        sg.Popup('-------- DADOS DO DIRETOR ----------', string_diretor)

    def seleciona_diretor(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR DIRETOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do diretor que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona diretor').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return id

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
