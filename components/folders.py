from PyQt5.QtWidgets import QWidget, QLabel, QListView, QVBoxLayout
from PyQt5 import QtGui

class FoldersView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color: rgb(25,25,25); margin:0px; border:3px solid rgb(0, 0, 0);")

        title = QLabel(self)
        title.setText("<font color='white'>Folders</font>")

        folder_list = QListView()
        model = QtGui.QStandardItemModel()
        folder_list.setModel(model)

        model.appendRow(QtGui.QStandardItem("E"))

        self.setAutoFillBackground(True)
        self.resize(int(self.parent().property("width")*0.2), int(self.parent().property("height")))
        self.backgroundColor = (0, 0, 0)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(folder_list)
        self.setLayout(layout)