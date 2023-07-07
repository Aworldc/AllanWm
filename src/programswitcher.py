from PySide6.QtWidgets import QLabel, QDialog, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QRect
from pyautogui import size as getScreenSize, getAllWindows, hotkey, getWindowsWithTitle


def fixbar():
    getWindowsWithTitle('AllanWm Bar')[0].restore()

def getWindows():
    windows = getAllWindows()
    bannedTitles = ["", "AllanWm Bar", "Program Manager", "Microsoft Text Input Application"]
    return [window for window in windows if (bannedTitles.count(window.title)) == 0]

def generateHandler(win, afterfn):
    def eeee(sig):
        if win.isMinimized:
            win.restore()
        else:
            win.minimize()
        afterfn()
    return eeee

def createDesktop(afterfn):
    def dtop(sig):
        for window in getWindows():
            window.minimize()
        afterfn()
    return dtop

class AllanWmProgramSwitcher(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowTitle("AllanWm Program Switcher")

        layout = QVBoxLayout()

        for window in getWindows():
            btn = QPushButton(window.title)
            btn.clicked.connect(generateHandler(window, self.accept))
            layout.addWidget(btn)

        layout.addSpacing(10)

        desktopbutton = QPushButton("Show desktop")
        desktopbutton.clicked.connect(createDesktop(self.accept))

        layout.addWidget(desktopbutton)

        closebutton = QPushButton("Cancel")
        closebutton.clicked.connect(self.reject)

        layout.addWidget(closebutton)

        self.setLayout(layout)
        fixbar()
    def update_pos(self):
        sw, sh = getScreenSize()
        self.setGeometry(QRect(((sw/2)-(self.width()/2)), 40, self.width(), self.height()))
        fixbar()
