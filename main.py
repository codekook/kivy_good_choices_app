'''

Simple application for creating chores and tracking their completion

'''

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import DictProperty, StringProperty

class GoodChoicesWidget(BoxLayout):

    pass 

class GoodChoicesChore(BoxLayout):

    user_input = TextInput()

    #notify me every time the button state changes
    def callback(instance):
        print('The button <%s> is being pressed' % instance.user_input)


class GoodChoicesList(BoxLayout):

    chore_list = DictProperty({})
    add_to_chorelist = Button()
    completed = ToggleButton()

    def add_chore(self):
        pass

class GoodChoicesApp(App):

    def build(self):
        gc = GoodChoicesWidget()
        self.new_user_input = GoodChoicesChore()
        self.new_chorelist = GoodChoicesList()
        gc.add_widget(self.new_user_input)
        gc.add_widget(self.new_chorelist)
        return gc
        

if __name__ == "__main__":
    GoodChoicesApp().run()