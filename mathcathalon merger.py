from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


# from main import BoxLayout


# while self.user.text != correct_answer:
class Math(App):

    def build(self):

        self.anchor1 = AnchorLayout(anchor_x="left", anchor_y="top")
        self.b1 = Button(text="Setings", size_hint=(None, None), size=("60dp", "60dp"), background_color='#00FFCE')
        self.anchor2 = AnchorLayout(anchor_x="right", anchor_y="top")
        self.b2 = Button(text="Calulator", size_hint=(None, None), size=("60dp", "60dp"), background_color='#00FFCE')
        self.anchor3 = AnchorLayout(anchor_x="center", anchor_y="top")
        self.b3 = Label(text="Mathcathalon", color='#00FFCE', size_hint=(None, None), font_size=(50))

        self.anchor1.add_widget(self.b1)
        self.anchor2.add_widget(self.b2)
        self.anchor3.add_widget(self.b3)
        boxlayout = BoxLayout()
        boxlayout.add_widget(self.anchor1)
        boxlayout.add_widget(self.anchor3)
        boxlayout.add_widget(self.anchor2)
        # return boxlayout
        # gridlayout = GridLayout()
        # gridlayout.add_widget(boxlayout)
        # gridlayout.add_widget(boxlayout)

        self.window = GridLayout(cols=1, size_hint=(.8, .8), pos_hint={"center_x": .5, "center_y": .5})
        self.window.add_widget(boxlayout)
        self.question = Label(text="10+10", font_size=50)
        self.remarks = Label(text="", color='#00FFCE', font_size=30)
        self.user = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, .5))
        self.button = Button(text="ok", size_hint=(1, .5), bold=True, background_color='#00FFCE')
        self.window.add_widget(self.question)
        self.window.add_widget(self.user)
        self.window.add_widget(self.remarks)
        self.window.add_widget(self.button)
        self.button.bind(on_press=self.sum)
        # self.user.bind(on_input=self.answer)
        return self.window
    def sum(self,add ):

        correct_answer = "20"
        question_1_answered = False
        answer_count = 0
        answer_limit = 3
        out_of_answers = False
        trys_count = 0
        trys_limit = 2
        out_of_trys = False
        global answer
        answer = 0

        while answer != correct_answer and not out_of_answers:
            if answer_count != answer_limit:
                answer = self.user.text
                answer_count += 1
                if trys_count != trys_limit and not out_of_trys:
                    if answer != correct_answer:
                        self.remarks.text = "try again"
                        trys_count += 1
                    if answer == correct_answer:
                        if answer_count == 1:
                             self.remarks.text = "***"
                        elif answer_count == 2:
                            self.remarks.text = "**"
                        elif answer_count == 3:
                            self.remarks.text = "*"
                else:
                    out_of_answers = True
                    break
        if out_of_answers:
            self.remarks.text = "you Loose"
        # else:
        #     self.remarks.text = "you win"


Math().run()
