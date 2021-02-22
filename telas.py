import PySimpleGUI as sg

class TelaGeral:

    menubar = [['AMBIENTE', ['CADASTRO DE SALAS', 'CONSULTA DE SALAS']],
                ['PARTICIPANTES', ['CADASTRO DE PARTICIPANTES', 'LISTA DE PARTICIPANTES', ]],
                ["SAIR"],]

    def __init__(self):
        layout = [
            [sg.Menu(TelaGeral.menubar)],
            [sg.Text('Nome', size=(7, 0)), sg.Input(size=(16, 0))],
            [sg.Text('Lotação', size=(7, 0)), sg.Input(size=(16, 0))],
            [sg.Radio('SALA1', "RADIO1", default=False), sg.Radio('SALA2', "RADIO2", default=False),
             sg.Radio('CAFÉ3', "RADIO3", default=False), sg.Radio('CAFÉ2', "RADIO4", default=False)],
            [sg.Button('cadastrar')], ]

        janela = sg.Window("titulo").layout(layout)

        self.button, self.values = janela.read()

    def iniciar(self):
        print(self.values)

tela = TelaGeral()
tela.iniciar()


