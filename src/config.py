from json import loads as parseJson


def readFileSync(path):
    with open(path, "r") as file:
        data = file.read()
    return data

class AllanWmTheme:
    def __init__(self, theme_object):
        self.object = theme_object
    def get_stylesheet(self):
        return f'''
            QMainWindow, QDialog {{
                background-color: {self.object['black']};
                border-bottom: 1px solid {self.object['white']}
            }}

            QDialog{{
                border: 1px solid {self.object['white']}
            }}

            QLabel, QPushButton {{
                color: {self.object['foreground']}
            }}

            * {{
                font-family: 'Fira code';
            }}

            QPushButton {{
                background-color: {self.object['selectionBackground']};
                border: none;
                padding: 2px 8px;
            }}

            QPushButton:hover {{
                border: 1px solid {self.object['cursorColor']};
            }}

            #BigPrick:hover {{
                background-color: {self.object['selectionBackground']};
                border-bottom: 1px solid {self.object['white']};
            }}

            #SmallPrick {{
                padding: 2px 8px;
                background-color: transparent;
            }}

            #SmallPrick:hover {{
                background-color: {self.object['selectionBackground']};
                border: none;
            }}
        '''

class AllanWmConfig:
    def __init__(self):
        self.config = parseJson(readFileSync(".allanwmrc"))

    def use_dark_theme(self):
        self.theme = "dark"
        return self

    def use_light_theme(self):
        self.theme = "light"
        return self

    def get_theme(self):
        return AllanWmTheme(self.config[self.theme])
