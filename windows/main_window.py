from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QSplitter

from toolbars import MainToolBar

from components import FoldersView, NotesView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Manager")
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)
        
        self.addToolBar(MainToolBar(self))

        splitter = QSplitter(Qt.Orientation.Horizontal, self)

        splitter.addWidget(FoldersView(self))
        splitter.addWidget(NotesView(self))

        splitter.setSizes([self.width() // 3, 2*self.width() // 3])

        layout = QHBoxLayout()
        layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)