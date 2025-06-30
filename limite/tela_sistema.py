import PySimpleGUI as sg

class TelaSistema:
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
            [sg.Text('-------- Premiação de filmes nacionais que não premia atores ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Membros Academia', "RD1", key='1')],
            [sg.Radio('Atores', "RD1", key='2')],
            [sg.Radio('Diretores', "RD1", key='3')],
            [sg.Radio('Filmes', "RD1", key='4')],
            [sg.Radio('Categorias', "RD1", key='5')],
            [sg.Radio('Votação', "RD1", key='6')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Premiação').Layout(layout)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
