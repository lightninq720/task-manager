from PyQt5.QtWidgets import QWidget, QLabel, QListView, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class NotesView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setStyleSheet("background-color: rgb(25,25,25); margin:0px; border:3px solid rgb(0, 0, 0); color:'white'")

        title = QLabel(self)
        title.setFont(QtGui.QFont('Arial', 20))
        title.setText("<font color='white'>Notes</font>")

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