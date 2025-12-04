
# ---------------------------------------------------------------
# Project : UE3 MenuBar (PyQt5)
# Author  : Marco Gernet
# Date    : 2025-12-04
# Purpose : MenuBar with PyQt5
# ---------------------------------------------------------------

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ue3_widget.ui', self)
        self.resize(800, 600)
        self.setWindowTitle("UE3:MenuBar")

        mb = self.menuBar()
        fm_1 = mb.addMenu("File")
        of = QAction("Open File", self)


        of.triggered.connect(self.fileOpener)
        fm_1.addAction(of)

        self.show()


    def fileOpener(self):

        (fname, ftype) = QFileDialog.getOpenFileName(self, "Open File",".","Text Files(*.txt)")

        if fname != "":



            # 1st variant
            self.textEdit.append("1st variant:\n")
            fo = open(fname, "r")


            #1st variant
            zeile = fo.readline()
            while zeile != "":
                l = len(zeile)-1
                if zeile[l] == "\n":
                  zeile = zeile[0:l]


                self.textEdit.append(zeile)
                zeile = fo.readline()

            self.textEdit.append("\n")
            fo.close()



            # 2nd variant
            self.textEdit.append("2nd variant:\n")
            fo = open(fname, "r")
            self.textEdit.append(fo.read())
            fo.close()

            self.textEdit.append("\n")



            # 3rd variant
            self.textEdit.append("3rd variant:\n")
            with open(fname) as fo:
                self.textEdit.append(fo.read())



app = QApplication([])
window = MainWindow()
app.exec_()