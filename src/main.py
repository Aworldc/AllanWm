from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
)

from PySide6.QtCore import Qt, QRect
from time import sleep
from pyautogui import size as getScreenSize, getActiveWindowTitle, getAllWindows
from datetime import datetime

from .config import AllanWmConfig
from .programlauncher import AllanWmProgramLauncher
from .programswitcher import AllanWmProgramSwitcher
from .calendar import AllanWmCalendar


class AllanWmBar(QMainWindow):
    def __init__(self):
        super().__init__()

        sw, sh = getScreenSize()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(0, 0, sw, 30)
        self.setFixedHeight(30)
        self.setWindowTitle("AllanWm Bar")

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.app_launcher = AllanWmBarAppLauncherWidget(self)
        self.active_window = AllanWmBarActiveWindowWidget()
        self.clock = AllanWmBarClockWidget()

        layout.addWidget(self.app_launcher)
        layout.addWidget(self.active_window)
        layout.addWidget(self.clock)

        widget = QWidget()
        widget.setGeometry(0, 0, sw, 30)
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def do_update(self):
        self.clock.do_update()
        self.active_window.do_update()

class AllanWmBarAppLauncherWidget(QWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow_parent = mainwindow

        layout = QHBoxLayout()
        layout.setContentsMargins(3, 0, 0, 0)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        startbutton = QPushButton(text="Start")
        startbutton.setFixedWidth(80)

        layout.addWidget(startbutton)
        startbutton.clicked.connect(self.start)

        workspace_1_btn = QPushButton(text=" 1 ")
        workspace_2_btn = QPushButton(text=" 2 ")
        workspace_3_btn = QPushButton(text=" 3 ")
        workspace_4_btn = QPushButton(text=" 4 ")
        workspace_5_btn = QPushButton(text=" 5 ")

        workspace_1_btn.setFixedWidth(30)
        workspace_2_btn.setFixedWidth(30)
        workspace_3_btn.setFixedWidth(30)
        workspace_4_btn.setFixedWidth(30)
        workspace_5_btn.setFixedWidth(30)

        layout.addWidget(workspace_1_btn)
        layout.addWidget(workspace_2_btn)
        layout.addWidget(workspace_3_btn)
        layout.addWidget(workspace_4_btn)
        layout.addWidget(workspace_5_btn)

        self.setLayout(layout)

    def start(self, signal):
        dlg = AllanWmProgramLauncher()
        dlg.show()
        dlg.update_pos()
        dlg.exec()

class AllanWmBarActiveWindowWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.windowlabel = QLabel("Loading...")
        self.windowlabel.setAlignment(Qt.AlignCenter)
        self.windowlabel.mousePressEvent = self.open_switcher
        self.windowlabel.setObjectName("BigPrick")

        layout.addWidget(self.windowlabel)

        self.setLayout(layout)

    def do_update(self):
        active_window = getActiveWindowTitle()
        self.windowlabel.setText(active_window)
    def open_switcher(self, event):
        ps = AllanWmProgramSwitcher()
        ps.show()
        ps.update_pos()
        ps.exec()

class AllanWmBarClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignRight)
        layout.setContentsMargins(0, 0, 7, 0)
        layout.setSpacing(0)

        self.cal = False

        self.clocklabel = QPushButton("Loading...")
        self.clocklabel.setObjectName("SmallPrick")

        self.clocklabel.clicked.connect(self.show_calendar)

        layout.addWidget(self.clocklabel)

        self.setLayout(layout)

    def do_update(self):
        now = datetime.now()
        self.clocklabel.setText(now.strftime("%H:%M:%S"))

        if self.cal != False:
            self.cal.do_update()
    def show_calendar(self):
        self.cal = AllanWmCalendar()
        self.cal.show()
        self.cal.update_pos()
        self.cal.finished.connect(self.hide_calendar)
        self.cal.open()
    def hide_calendar(self):
        self.cal = False

def main():
    app = QApplication([])

    app_config = AllanWmConfig()
    app_config.use_dark_theme()

    app.setStyleSheet(app_config.get_theme().get_stylesheet())

    window = AllanWmBar()
    window.show()

    while True:
        QApplication.processEvents()
        window.do_update()
        sleep(0.01)
