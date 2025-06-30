import PySimpleGUI as sg

class TelaVotacao():
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
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- VOTACAO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Voto', "RD1", key='1')],
            [sg.Radio('Listar Votos', "RD1", key='2')],
            [sg.Radio('Excluir Voto', "RD1", key='3')],
            [sg.Radio('Visualizar vencedores', "RD1", key='4')],
            [sg.Radio('Top 3 Filmes Vencedores', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Votação').Layout(layout)

    def pega_dados_voto(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS DO VOTO ----------', font=("Helvica", 25))],
            [sg.Text('ID do votante:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Text('Nome da Categoria:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Vencedor:', size=(15, 1)), sg.InputText('', key='votado')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Voto').Layout(layout)

        button, values = self.open()
        id_membro = values['id']
        nome_categoria = values['nome']
        votado = values['votado']

        self.close()
        return {"id": id_membro, "nome": nome_categoria, "votado": votado}

    def mostra_voto(self, dados_voto):
        string_voto = ""
        string_voto = string_voto + "MEMBRO: " + dados_voto['votante'] + '\n'
        string_voto = string_voto + "CATEGORIA: " + dados_voto['categoria'] + '\n'
        string_voto = string_voto + "VENCEDOR: " + dados_voto['votado'] + '\n\n'

        sg.Popup('-------- DETALHES DO VOTO ----------', string_voto)

    def pega_categoria(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('---ESCOLHA A CATEGORIA---', font=("Helvica", 25))],
            [sg.Text('Categoria:', size=(15, 1)), sg.InputText('', key='categoria')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Escolha a Categoria').Layout(layout)

        button, values = self.open()
        categoria = values['categoria']

        self.close()
        return categoria

    def seleciona_voto(self):
        sg.theme('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR VOTO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do votante que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID do votante:', size=(15, 1)), sg.InputText('', key='id_voto')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona voto').Layout(layout)

        button, values = self.open()
        id_voto = values['id_voto']
        self.close()
        return id_voto

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
