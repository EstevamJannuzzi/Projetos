from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VendasWindows(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def add_produto_codigo(self, codigo):
        pass

    def add_produto_nome(self, nome):
        pass
    
    def admin(self):
        pass

    def sair(self):
        pass

    def deletar(self):
        pass

    def atualizar(self):
        pass


class VendasApp(App):
    def build(self):
        return VendasWindows()
    

if __name__ == '__main__':
    VendasApp().run()
