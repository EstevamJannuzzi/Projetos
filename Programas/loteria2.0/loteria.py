from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Lotery(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def um(self):
        self.ids.txt_1.text = '1'
    
    def dois(self):
        self.ids.txt_2.text = '2'

    def tres(self):
        self.ids.txt_3.text = '3'

    def quatro(self):
        self.ids.txt_4.text = '4'

    def cinco(self):
        self.ids.txt_5.text = '5'

    def seis(self):
        self.ids.txt_6.text = '6'

    def sete(self):
        self.ids.txt_7.text = '7'

    def oito(self):
        self.ids.txt_8.text = '8'

    def nove(self):
        self.ids.txt_9.text = '9'

    def dez(self):
        self.ids.txt_10.text = '10'


class Loteria(App):
    def build(self):
        return Lotery()
    

if __name__=='__main__':
    Loteria().run()
