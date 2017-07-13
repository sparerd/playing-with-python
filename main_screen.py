import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QListView)
from PyQt5.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 600)
        self.list_view = QListView()

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.list_view)

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)
        self.show()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
