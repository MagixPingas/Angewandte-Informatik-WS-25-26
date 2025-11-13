from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('beispiel_5.ui', self)
        self.rb_1.toggled.connect(self.toggleTest)
        self.rb_2.toggled.connect(self.toggleTest)
        self.rb_3.toggled.connect(self.toggleTest)
        self.resize(800, 600)
        self.setWindowTitle("Beispiel 5")
        self.show()


    def toggleTest(self):
        rb = self.sender()

        if rb.isChecked():
            print(rb.objectName(), 'ist aktiv!')






app = QApplication([])
window = MainWindow()
app.exec_()