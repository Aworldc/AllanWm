from PySide6.QtWidgets import QLabel, QDialog, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QRect
from pyautogui import size as getScreenSize
from datetime import datetime


class AllanWmCalendar(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowTitle("AllanWm Calendar")

        layout = QVBoxLayout()

        self.clocklabel = QLabel("Loading...")
        layout.addWidget(self.clocklabel)

        layout.addSpacing(10)

        closebutton = QPushButton("Ok")
        closebutton.clicked.connect(self.reject)

        layout.addWidget(closebutton)

        self.setLayout(layout)
    def update_pos(self):
        sw, sh = getScreenSize()
        self.setGeometry(QRect(((sw - 10) - self.width()), 40, self.width(), self.height()))
    def do_update(self):
        now = datetime.now()
        self.clocklabel.setText(now.strftime("%H:%M:%S"))