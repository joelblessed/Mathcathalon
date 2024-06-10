from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class AnchorLayout(AnchorLayout):
   pass
class AnchorLayoutPause(AnchorLayout):
    pass
class AnchorLayoutSettings(AnchorLayout):
    pass
class AnchorLayoutQuit(AnchorLayout):
    pass
class GridLayout(GridLayout):

    pass
class BoxLayout(BoxLayout):
    pass
class Canvas(Widget):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text="A")
    #     b2 = Button(text="b")
    #     self.add_widget(b1)
    #     self.add_widget(b2)






class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

if __name__== '__main__':
 TheLabApp().run()
