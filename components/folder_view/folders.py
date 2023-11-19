from PyQt5.QtWidgets import QWidget, QLabel, QListView, QVBoxLayout
from PyQt5 import QtGui
import json
from dataclasses import dataclass
from typing import List, Dict

class FoldersView(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.data = self.readReminders()

        self.setStyleSheet("background-color: rgb(25,25,25); margin:0px; border:3px solid rgb(0, 0, 0); color:'white'")

        title = QLabel(self)
        title.setFont(QtGui.QFont('Arial', 20))
        title.setText("<font color='white'>Folders</font>")

        folder_list = QListView()
        model = QtGui.QStandardItemModel()
        folder_list.setModel(model)

        for i in self.data:
            model.appendRow(FolderView(i))

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(folder_list)
        self.setLayout(layout)

    def readReminders(self):
        with open("./data/reminders.json") as f:
            data = json.load(f)
            return data

class FolderView(QtGui.QStandardItem):
    def __init__(self, folder):
        super().__init__()
        self._folder = FolderData(**folder)
        self.setText(self.title)

    @property
    def title(self):
        return self._folder.title

@dataclass
class FolderData:
    folder_id: str
    title: str
    description: str
    notes: List[Dict[str, str]]
    