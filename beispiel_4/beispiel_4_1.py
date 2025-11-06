from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('beispiel_4_1_widget.ui', self)
        self.lineEdit.textChanged.connect(self.textSetting)
        self.resize(800, 600)
        self.setWindowTitle("Beispiel 4")
        self.show()


    def textSetting(self, value):
        self.label.setText(value)

app = QApplication([])
window = MainWindow()
app.exec_()