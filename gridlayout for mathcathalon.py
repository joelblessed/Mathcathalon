from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class sample(App):
    def build(self):

        self.window = GridLayout(cols = 1,size_hint = (.8,.8),pos_hint = {"center_x":.5,"center_y":.5})
        self.window.add_widget(Label(text="Mathcathalon",color = '#00FFCE',font_size = 30))
        self.question = Label(text = "10 + 10",)
        self.remarks = Label(text = "",color = '#00FFCE',font_size = 18)
        self.user = TextInput(multiline=False,padding_y = (20,20),size_hint = (1,.5))
        self.button = Button(text="ok",size_hint = (1,.5),bold = True,background_color = '#00FFCE')
        self.window.add_widget(self.question)
        self.window.add_widget(self.user)
        self.window.add_widget(self.remarks)
        self.window.add_widget(self.button)
        self.button.bind(on_press = self.sum)

        return self.window

    def sum(self,add):

        if self.user.text != "20":
           self.remarks.text = "ewwwh"
        else:
            self.remarks.text = self.user.text + " good job"

sample().run()
