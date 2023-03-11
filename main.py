from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, ObjectProperty, StringProperty

class GoodChoicesApp(App):

    def build(self):
        chore_layout = BoxLayout(orientation="vertical")
        chore_input = TextInput(font_size=50, 
                        size_hint_y=None, 
                        multiline=False,
                        height=200,
                        text="Add a Chore")
        chore_list = GridLayout(rows=2, cols=2)
        list_item = Label(text="List of Chores",
                        font_size=50)
        completed_chore = ToggleButton(text="Completed", 
                                    state="normal")
        
        chore_input.bind(text=list_item.setter('text'))

        chore_list.add_widget(list_item)
        chore_list.add_widget(completed_chore)
        chore_layout.add_widget(chore_input)
        chore_layout.add_widget(chore_list)
        return chore_layout

if __name__ == "__main__":
    GoodChoicesApp().run()