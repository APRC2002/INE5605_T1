import PySimpleGUI as sg

class TelaMembroAcademia():
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
            [sg.Text('-------- ACADEMIA ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Membro', "RD1", key='1')],
            [sg.Radio('Alterar Membro', "RD1", key='2')],
            [sg.Radio('Listar Membros', "RD1", key='3')],
            [sg.Radio('Excluir Membro', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Academia').Layout(layout)

    def pega_dados_membroAcademia(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS MEMBROS ACADEMIA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.InputText('', key='data_de_nascimento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Membro da Academia').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        nacionalidade = values['nacionalidade']
        data_de_nascimento = values['data_de_nascimento']

        self.close()
        return {"nome": nome, "nacionalidade": nacionalidade, "data_de_nascimento": data_de_nascimento}

    def mostra_membroAcademia(self, dados_membroAcademia):
        string_membro = ""
        for dado in dados_membroAcademia:
            string_membro = string_membro + "NOME DO MEMBRO: " + dado["nome"] + '\n'
            string_membro = string_membro + "ID DO MEMBRO: " + str(dado["ID"]) + '\n'
            string_membro = string_membro + "NACIONALIDADE DO MEMBRO: " + dado["nacionalidade"] + '\n'
            string_membro = string_membro + "DATA DE NASCIMENTO DO MEMBRO: " + dado["data_de_nascimento"] + '\n\n'

        sg.Popup('-------- DADOS DO MEMBRO DA ACADEMIA ----------', string_membro)

    def seleciona_membroAcademia(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR MEMBRO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do membro que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona membro').Layout(layout)

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