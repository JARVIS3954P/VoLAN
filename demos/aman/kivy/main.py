import kivy
from kivy.app import App
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class Stack_layout_example(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b = Button(text = "Z", size_hint =(.2,.2))
        self.add_widget(b)

#class anchor_layout_example(AnchorLayout):
#    pass

#class Box_layout_example(BoxLayout):
#    pass

class first_widget(Widget):
    pass

class firstApp(App):
    pass

app = firstApp()
app.run()
