from PyQt5.QtWidgets import QWidget, QApplication
from windows import MainWindow

app = QApplication([])
app.setQuitOnLastWindowClosed(True)

mainWindow = MainWindow()
mainWindow.show()

app.exec()