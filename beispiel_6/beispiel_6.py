from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('beispiel_6.ui', self)
        self.horizontalSlider.valueChanged.connect(self.sliderBoxChanged)
        self.spinBox.valueChanged.connect(self.sliderBoxChanged)
        self.resize(800, 600)
        self.setWindowTitle("Beispiel 6")
        self.show()


    def sliderBoxChanged(self, value):
        self.spinBox.setValue(value)
        #blockSignals einfügen!
        self.horizontalSlider.setValue(value)
        print(value)







app = QApplication([])
window = MainWindow()
app.exec_()