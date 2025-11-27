from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('beispiel_7.ui', self)
        self.listWidget.addItem("Hallo")
        self.listWidget.addItem("Hallo Welt")
        self.listWidget.itemPressed.connect(self.listTest)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        print(f"Anzahl der Items: {self.listWidget.count()}")
        self.resize(800, 600)
        self.setWindowTitle("Beispiel 7")
        self.show()


    def listTest(self, item):
        r = self.listWidget.indexFromItem(item).row()
        print(f"Zeile {r}; Item-Text = {item.text()}")

        print([item.text() for item in self.listWidget.selectedItems()])





app = QApplication([])
window = MainWindow()
app.exec_()