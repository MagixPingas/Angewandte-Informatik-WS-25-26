from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.show()

        (fname, ftype) = QFileDialog.getOpenFileName(self, "Datei öffnen", "..\\angewendte_info", "Python Files(*.py);;Text Files(*.txt);;C++ Files(*.cpp)")

        if fname != "":
            fo = open(fname, "r")


            for line in fo:
                print(line, end="")

            fo.close()




app = QApplication([])
window = MainWindow()
app.exec_()