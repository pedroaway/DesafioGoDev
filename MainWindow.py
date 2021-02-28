import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from interface import Ui_MainWindow


class MainWindow:
    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.Dados = []
        self.Salas = []
        self.tabela = self.frame()
        self.distribuir = ['sala1', 'sala2', 'café1', 'café2']


#BOTÕES PARA MUDAR AS PÁGINAS NA APLICAÇÃO
        self.ui.TELAS.setCurrentWidget(self.ui.page3)
        self.ui.botao1.clicked.connect(self.showtela1)
        self.ui.botao2.clicked.connect(self.showtela2)
        self.ui.botao3.clicked.connect(self.showtela3)
        self.ui.botao4.clicked.connect(self.showtela4)
        self.ui.botao5.clicked.connect(self.showtela5)
#BOTÕES DE INTERAÇÃO
        self.ui.botao4_5.clicked.connect(self.cadastrarparticipantes)
        self.ui.botao4_5.clicked.connect(self.mostrarframe)
        self.ui.botao4_6.clicked.connect(self.cadastrarsalas)
        self.ui.botao4_6.clicked.connect(self.frameSalas)
        self.ui.botao4_6.clicked.connect(self.mostrar_frame_salas)


#FUNÇÕES QUE CONECTAM OS BOTÕES COM AS PÁGINAS E FAZEM A MUDANÇA
    def show(self):
        self.main_win.show()
    def showtela1(self):
        self.ui.TELAS.setCurrentWidget(self.ui.page1)
    def showtela2(self):
        self.ui.TELAS.setCurrentWidget(self.ui.page2)
    def showtela3(self):
        self.ui.TELAS.setCurrentWidget(self.ui.page3)
    def showtela4(self):
        self.ui.TELAS.setCurrentWidget(self.ui.page4)
    def showtela5(self):
        self.ui.TELAS.setCurrentWidget(self.ui.page5)

    def cadastrarparticipantes(self):
        NomeParticipante = self.ui.lineEdit_8.text()
        SobrenomeParticipante = self.ui.lineEdit_9.text()
        linha = [NomeParticipante, SobrenomeParticipante]
        self.Dados.append(linha)
        print(self.Dados)

    def cadastrarsalas(self):
        descricao = []
        lotacao = self.ui.lineEdit_11.text()
        objeto = [descricao, lotacao]

        if self.ui.radioButton.isChecked():
            descricao.append('sala1')
        elif self.ui.radioButton_2.isChecked():
            descricao.append('sala2')
        elif self.ui.radioButton_3.isChecked():
            descricao.append('café1')
        elif self.ui.radioButton_4.isChecked():
            descricao.append('café2')
        else:
            descricao.append('sala não cadastrada')
        self.Salas.append(objeto)


#DATA-FRAMES
    def frame(self):
        lstDados = self.Dados
        dfa = pd.DataFrame(columns=['nome',' sobrenome',], data=lstDados)
        return dfa

    def frameSalas(self):
        lstDados = self.Salas
        dfa = pd.DataFrame(columns=['descrição',' lotação'], data=lstDados)
        return dfa
#FUNÇÕES PARA MOSTRAR OS DATA-FRAMES
    def mostrarframe(self):
        dcr = self.frame()
        self.ui.textEdit.setText(str(dcr))

    def mostrar_frame_salas(self):
        dcr = self.frameSalas()
        self.ui.textEdit_3.setText(str(dcr))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
