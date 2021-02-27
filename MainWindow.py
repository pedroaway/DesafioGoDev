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



#BOTÕES PARA MUDAR AS PÁGINAS NA APLICAÇÃO

        self.ui.TELAS.setCurrentWidget(self.ui.page1)
        self.ui.botao1.clicked.connect(self.showtela1)
        self.ui.botao2.clicked.connect(self.showtela2)
        self.ui.botao3.clicked.connect(self.showtela3)
        self.ui.botao4.clicked.connect(self.showtela4)
        self.ui.botao5.clicked.connect(self.showtela5)
#BOTAO TELA 1
        self.ui.botao4_5.clicked.connect(self.cadastrarparticipantes)
        self.ui.botao4_5.clicked.connect(self.frame)
        self.ui.botao4_5.clicked.connect(self.mostrarframe)
#BOTAO TELA 3

#EXIBIR PARTICIPANTES

       # self.ui.botao4_6.clicked.connect(self.cadastrarsalas)
#EXTRAÇÃO DE DADOS

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


#TELA1
    def cadastrarparticipantes(self):
        NomeParticipante = self.ui.lineEdit_8.text()
        SobrenomeParticipante = self.ui.lineEdit_9.text()
        linha = [NomeParticipante, SobrenomeParticipante]
        self.Dados.append(linha)
        print(self.Dados)



    def frame(self):
        lstDados = self.Dados
        dfa = pd.DataFrame(columns=['__Nome__   ', '   __Nobrenome__', 'sala1', 'sala1', 'café2'], data=lstDados)
        return dfa

#TELA2
    def mostrarframe(self):
        dcr = self.frame()
        print(dcr)
        self.ui.textEdit.setText(str(dcr))



#TELA3
    def cadastrarsalas(self):
        descricao = self.ui.lineEdit_10.text()
        lotacao = self.ui.lineEdit_11.text()
        tipo = "indefinido"
        if self.ui.radioButton.isChecked():
            tipo = ("Sala1")
        elif self.ui.radioButton_2.isChecked():
            tipo = ("Sala2")
        elif self.ui.radioButton_3.isChecked():
            tipo = ("Saladecafé1")
        elif self.ui.radioButton_4.isChecked():
            tipo = ("Saladecafé2")

        item = [descricao, lotacao, tipo]
        self.Salas.append(item)
        return self.Salas

#DATA_FRAME



   #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
