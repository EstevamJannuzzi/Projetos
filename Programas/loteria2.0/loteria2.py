'''from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Lotery(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Loteria(App):
    def build(self):
        return Lotery()
    

if __name__=='__main__':
    Loteria().run()
