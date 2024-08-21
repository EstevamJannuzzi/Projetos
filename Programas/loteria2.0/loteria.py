from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Lotery(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def um(self):
        self.ids.escolhas.text = '1'
    
    def dois(self):
        self.ids.escolhas.text = '2'

    def tres(self):
        self.ids.escolhas.text = '3'


class Loteria(App):
    def build(self):
        return Lotery()
    

if __name__=='__main__':
    Loteria().run()
