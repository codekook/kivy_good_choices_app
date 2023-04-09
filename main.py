'''

Simple application for creating chores and tracking their completion

'''
import json 
from os.path import join, exists 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import AliasProperty, StringProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock

#adds the funciontionality to create new chores and edit existing chores
class MutableTextInput(FloatLayout):
    text = StringProperty()
    
    def __init__(self, **kwargs):
        super(MutableTextInput, self).__init__(**kwargs)
        Clock.schedule_once(self.prepare, 0)
    
    def prepare(self, *args):
        self.w_label = self.ids.w_label.__self__
        self.view()
    
    def on_touch_down(self, touch):
        pass 

    def edit(self):
        pass 

    def view(self): 
        pass 

    def check_focus_and_view(self, textinput):
        pass 

class GoodChoices(Screen):

    data = ListProperty()
    print('data: ', data)

    def _get_widgets_data(self):
        return [{
            'chore_index': index,
            'chore_description': item['description']
            }
            for index, item in enumerate(self.data)]

    data_for_widgets = AliasProperty(_get_widgets_data, bind=['data']) 

class GoodChoicesChore(BoxLayout):

    chore_index = NumericProperty()
    chore_description = StringProperty()


class GoodChoiceView(Screen):

    chore_index = NumericProperty()
    chore_description = StringProperty()


class GoodChoicesApp(App):

    def build(self):
        self.chores = GoodChoices(name="chores")
        self.load_chores()

        self.transition = SlideTransition(duration=.35)
        root = ScreenManager(transition=self.transition)
        root.add_widget(self.chores)
        return root
    
    def load_chores(self):
        if not exists(self.chores_fn):
            return
        with open(self.chores_fn) as fd:
            data = json.load(fd)
        self.chores.data = data 

    def save_chores(self):
        pass 

    def del_chore(self):
        pass 

    def edit_chore(self):
        pass 

    def add_chore(self):
        pass 

    def set_chore_description(self, chore_index, chore_description):
        self.chores.data[chore_index]['description'] = chore_description 
        self.save_chores() 
        self.refresh_chores() 
    
    def refresh_chores(self):
        pass 

    def go_chores(self):
        pass 
    
    @property #adds additional getter and setter functionality to chores_fn()
    def chores_fn(self):
        return join(self.user_data_dir, 'chores.json')
        

if __name__ == "__main__":
    GoodChoicesApp().run()