from MainWindow import MainWindow


class dados():

    def DividirParticipantes(self):
        info = MainWindow()
        info.informacoes1()
        limite_de_pessoas = int(20)
        sala1 = [""]
        sala2 = [""]
        array_alunos = [info.informacoes1()]
        x = 1
        y = 0
        if sala1 < sala2:
           sala1.append(array_alunos[y+x])
           y = y+x
        elif sala2 < sala1:
           sala1.append(array_alunos[y+x])
           y = y+x
        
        print(sala1)



dados()