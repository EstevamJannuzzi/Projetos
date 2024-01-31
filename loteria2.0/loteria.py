import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton


class Loteria(App):
    def build(self):
        superBox = BoxLayout(orientation = 'vertical')
        HB = BoxLayout(orientation = 'horizontal')

        b1 = ToggleButton(text='1', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b2 = ToggleButton(text='2', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b3 = ToggleButton(text='3', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b4 = ToggleButton(text='4', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b5 = ToggleButton(text='5', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b6 = ToggleButton(text='6', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b7 = ToggleButton(text='7', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b8 = ToggleButton(text='8', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b9 = ToggleButton(text='9', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))
        b10 = ToggleButton(text='10', background_color = (1, 0, 1), font_size = 32, size_hint = (0.2, 0.2))

        HB.add_widget(b1)
        HB.add_widget(b2)
        HB.add_widget(b3)
        HB.add_widget(b4)
        HB.add_widget(b5)
        HB.add_widget(b6)
        HB.add_widget(b7)
        HB.add_widget(b8)
        HB.add_widget(b9)
        HB.add_widget(b10)

        superBox.add_widget(HB)

        return superBox


Loteria().run()
