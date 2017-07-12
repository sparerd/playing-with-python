# must install pyqt5 using: pip install pyqt5
import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    
    # build a window
    window = QtWidgets.QWidget()
    window.setGeometry(2500, 100, 300, 200)  # x, y, width, height
    window.setWindowTitle('PyQt5 tutorials')

    # build a text label
    label1 = QtWidgets.QLabel("hello world")

    # build a picture label
    label2 = QtWidgets.QLabel(window)
    label2.setPixmap(QtGui.QPixmap("information.png"))
    label2.move(120, 90)

    # build a button
    button = QtWidgets.QPushButton("Push me")

    # horizontal box layout
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(label1)
    h_box.addStretch()

    # verticle box layout
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(button)
    v_box.addLayout(h_box)

    window.setLayout(v_box)

    # show window / execute program loop
    window.show()
    sys.exit(app.exec_())

# window()


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.button = QtWidgets.QPushButton("Push me")
        self.button_print = QtWidgets.QPushButton("Print")
        self.label = QtWidgets.QLabel("I have not been clicked")
        self.txt_edit = QtWidgets.QLineEdit()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.label)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.txt_edit)
        v_box.addWidget(self.button)
        v_box.addWidget(self.button_print)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt5 lesson 5")

        self.button.clicked.connect(self.btn_clicked)
        self.button_print.clicked.connect(self.btn_clicked)

        self.show()

    def btn_clicked(self):
        sender = self.sender()
        if sender.text() == "Print":
            print(self.txt_edit.text())
        else:
            self.label.setText("I have been clicked")
            self.txt_edit.setText("")

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
