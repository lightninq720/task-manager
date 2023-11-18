from PyQt5.QtWidgets import QWidget, QLabel, QListView, QVBoxLayout
from PyQt5 import QtGui

class NotesView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # self.setStyleSheet("background-color: rgb(25,25,25); margin:0px; border:0px solid rgb(0, 0, 0);")

        title = QLabel(self)
        title.setText("Notes")

        notes_list = QListView()
        model = QtGui.QStandardItemModel()
        notes_list.setModel(model)

        model.appendRow(QtGui.QStandardItem("E"))

        self.setAutoFillBackground(True)
        self.backgroundColor = (0, 0, 0)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(notes_list)
        self.setLayout(layout)