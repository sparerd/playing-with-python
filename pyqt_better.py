import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget, QCheckBox, QRadioButton)
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.b1 = QPushButton("Clear")
        self.b2 = QPushButton("Print")
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(50)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.chk = QCheckBox("Do you like dogs?")
        self.radDog = QRadioButton("Dogs")
        self.radCat = QRadioButton("Cats")

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)
        v_box.addWidget(self.chk)
        v_box.addWidget(self.radDog)

        self.setLayout(v_box)
        self.setWindowTitle("Testing")

        self.b1.clicked.connect(lambda: self.btn_click(self.b1, "hello from Clear"))
        self.b2.clicked.connect(lambda: self.btn_click(self.b2, "hello from Print"))
        self.s1.valueChanged.connect(self.v_change)
        self.chk.clicked.connect(lambda: self.chk_change(self.chk.isChecked(), self.le))

        self.show()

    def btn_click(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v_change(self):
        val = str(self.s1.value())
        self.le.setText(val)

    def chk_change(self, checked, le):
        if checked:
            le.setText("You like dogs!")
        else:
            le.setText("You don't like dogs...")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
