from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VendasWindows(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VendasApp(App):
    def build(self):
        return VendasWindows()
    

if __name__ == '__main__':
    VendasApp().run()
