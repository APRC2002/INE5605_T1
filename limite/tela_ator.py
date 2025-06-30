import PySimpleGUI as sg

class TelaAtor():
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
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- ATOR ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Alterar Ator', "RD1", key='1')],
            [sg.Radio('Listar Atores', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Atores').Layout(layout)

    def pega_dados_ator(self, genero_esperado):
        sg.theme('DarkTeal4')
        if genero_esperado == "M":
            titulo = "-------- DADOS ATOR ----------"
        elif genero_esperado == "F":
            titulo = "-------- DADOS ATRIZ ----------"
        
        layout = [
            [sg.Text(titulo, font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText('', key='data_de_nascimento')],
            [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Ator').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        data_de_nascimento = values['data_de_nascimento']
        nacionalidade = values['nacionalidade']
        genero = genero_esperado

        self.close()
        return {"nome": nome, "data_de_nascimento": data_de_nascimento, "nacionalidade": nacionalidade, "genero": genero}

    def mostra_ator(self, dados_ator):
        string_ator = ""
        for dado in dados_ator:
            string_ator = string_ator + "ID DO ATOR: " + str(dado["id"]) + '\n'
            string_ator = string_ator + "NOME DO ATOR: " + dado["nome"] + '\n'
            string_ator = string_ator + "DATA DE NASCIMENTO DO ATOR: " + dado["data_de_nascimento"] + '\n'
            string_ator = string_ator + "NACIONALIDADE DO ATOR: " + dado["nacionalidade"] + '\n'
            string_ator = string_ator + "GENERO DO ATOR: " + dado["genero"] + '\n\n'

        sg.Popup('-------- DADOS DO ATOR ----------', string_ator)

    def seleciona_ator(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR ATOR ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do ator que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona ator').Layout(layout)

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
