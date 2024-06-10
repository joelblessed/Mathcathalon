from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label




class Math(App):
    def build(self):
        self.anchor1 = AnchorLayout(anchor_x = "left",anchor_y="top")
        self.b1 = Button(text="Setings", size_hint = (None,None),size= ("60dp","60dp"))
        self. anchor2 = AnchorLayout(anchor_x = "right",anchor_y = "top")
        self.b2 = Button(text = "Pause", size_hint = (None,None),size= ("60dp","60dp") )
        self.anchor3 = AnchorLayout(anchor_x="center",anchor_y = "top")
        self.b3 = Label(text="Mathcathalon", size_hint=(None, None), font_size = (50))
        self.anchor1.add_widget(self.b1)
        self.anchor2.add_widget(self.b2)
        self.anchor3.add_widget(self.b3)
        boxlayout = BoxLayout()
        boxlayout.add_widget(self.anchor1)
        boxlayout.add_widget(self.anchor3)
        boxlayout.add_widget(self.anchor2)
        return boxlayout
Math().run()