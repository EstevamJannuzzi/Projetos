from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Programa(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Aplicativo(App):
    def build(self):
        return Programa()
    

if __name__=='__main__':
    Aplicativo().run()