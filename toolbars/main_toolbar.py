from PyQt5.QtWidgets import QToolBar, QStatusBar
from PyQt5.QtCore import Qt

class MainToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setMovable(False)