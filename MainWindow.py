import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from interface import Ui_MainWindow


"""def funcao_principal():
    return("0")

def mudar_telas():
    main_win = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_win)

    ui.botao1.clicked.connect(ui.page1)
    ui.botao2.clicked.connect(ui.page2)

def show(self):
    self.main_win.show()

def show1(self):
    self.ui.StackedWidget.SetCurrentWidget(self.ui.page1)

def show2(self):
    self.ui.StackedWidget.SetCurrentWidget(self.ui.page2)


app = QtWidgets.QApplication([])
interface = uic.loadUi("interface.ui")

interface.show()
app.exec()"""


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.TELAS.setCurrentWidget(self.ui.page1)

        self.ui.botao1.clicked.connect(self.showtela1)
        self.ui.botao2.clicked.connect(self.showtela2)
        self.ui.botao3.clicked.connect(self.showtela3)
        self.ui.botao4.clicked.connect(self.showtela4)
        self.ui.botao5.clicked.connect(self.showtela5)

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





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())