from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.show()

        (text, ok) = QInputDialog.getText(self, "Wichtige Frage!", "Ihr Name")

        print(ok)
        if ok:
            msg = QMessageBox(self)
            msg.setText("Hallo " + text)
            msg.exec_()

app = QApplication([])
window = MainWindow()
app.exec_()