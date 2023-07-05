from json import loads as parseJson
from fs import readFileSync

class AllanWmTheme():
    def __init__(self, theme_object):
        self.object = theme_object
    
    def get_color(self, name):
        return self.object[name]

class AllanWmConfig():
    def __init__(self):
        self.config = parseJson(readFileSync(".allanwmrc"))

    def use_dark_theme(self):
        self.theme = 'dark'
    
    def use_light_theme(self):
        self.theme = 'light'
    
    def get_theme(self):
        return AllanWmTheme(self.config[self.theme])