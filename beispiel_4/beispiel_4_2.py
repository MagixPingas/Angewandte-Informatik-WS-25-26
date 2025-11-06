from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('beispiel_4_2_widget.ui', self)
        self.comboBox.activated.connect(self.comboBoxInput)
        self.comboBox.addItem("D")
        self.resize(800, 600)
        self.setWindowTitle("Beispiel 4")
        self.show()


    def comboBoxInput(self):
        index = self.comboBox.currentIndex()
        input = self.comboBox.currentText()
        print('index = ', index, 'input = ', input)


app = QApplication([])
window = MainWindow()
app.exec_()