from PySide6.QtWidgets import QLabel, QDialog, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from os import listdir, startfile
from os.path import isfile, join
from operator import itemgetter


def chunkify(list, size):
    outputlist = []
    for i in range(0, len(list), size):
        outputlist.append(list[i : i + size])
    return outputlist


def getPrograms():
    user_programs_path = (
        "C:\\Users\\Allan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
    )
    global_programs_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    user_programs = [
        {"base":user_programs_path,"end":f} for f in listdir(user_programs_path) if isfile(join(user_programs_path, f))
    ]
    global_programs = [
        {"base":global_programs_path,"end":f}
        for f in listdir(global_programs_path)
        if isfile(join(global_programs_path, f))
    ]

    return [x for x in (sorted(user_programs + global_programs, key=itemgetter('end'))) if x['end'] != "desktop.ini"]


def createAsshole(program, afterfn):
    def asshole():
        startfile(program)
        afterfn()
    return asshole


class AllanWmProgramLauncher(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowTitle("AllanWm Program Launcher")

        layout = QVBoxLayout()

        title = QLabel("Start")

        for programgroup in chunkify(getPrograms(), 6):
            widget = QWidget()
            sublayout = QHBoxLayout()
            sublayout.setContentsMargins(0, 0, 0, 0)

            for program in programgroup:
                progbtn = QPushButton(program['end'][:-4])
                progbtn.clicked.connect(createAsshole(f"{program['base']}\\{program['end']}", self.accept))
                sublayout.addWidget(progbtn)

            widget.setLayout(sublayout)
            layout.addWidget(widget)
        
        layout.addSpacing(10)

        closebutton = QPushButton("Cancel")
        closebutton.clicked.connect(self.reject)

        layout.addWidget(closebutton)

        self.setLayout(layout)
