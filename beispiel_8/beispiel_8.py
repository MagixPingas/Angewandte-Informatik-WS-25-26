from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mb = self.menuBar()
        fm_1 = mb.addMenu("File")
        fm_2 = mb.addMenu("Edit")

        actionSchliessen = QAction("Close Window", self)
        actionSchliessen.triggered.connect(self.close)
        actionTest = QAction("Open File", self)
        actionTest.triggered.connect(self.close)
        fm_1.addAction(actionSchliessen)
        fm_1.addAction(actionTest)

        self.resize(800, 600)
        self.setWindowTitle("Beispiel 8")
        self.show()



app = QApplication([])
window = MainWindow()
app.exec_()