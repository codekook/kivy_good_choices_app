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
from kivy.uix.widget import Widget
from kivy.properties import AliasProperty, StringProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.animation import Animation 
from random import randint

#adds the interactive functionality to each element of the graphical interface 
class MutableTextInput(FloatLayout):

    text = StringProperty()
    
    def __init__(self, **kwargs):
        super(MutableTextInput, self).__init__(**kwargs)
        Clock.schedule_once(self.prepare, 0)
    
    def prepare(self, *args):
        #displays the chore
        self.w_label = self.ids.w_label.__self__

        #makes chore editable
        self.w_textinput = self.ids.w_textinput.__self__
        
        self.view()
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            self.edit()
        return super(MutableTextInput, self).on_touch_down(touch) 

    def edit(self):
        pass
        self.clear_widgets()
        self.add_widget(self.w_textinput)
        self.w_textinput.focus = True

    def view(self): 
        self.clear_widgets() 
        if not self.text:
            self.w_label.tet = 'Double tap/click to edit'
        self.add_widget(self.w_label) 

    def check_focus_and_view(self, textinput):
        if not textinput.focus:
            self.text = textinput.text
            self.view()

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


class GoodChoicesView(Screen):

    chore_index = NumericProperty()
    chore_description = StringProperty()

class CelebrateView(Screen):

    pass

class GoodChoicesApp(App):

    def build(self):
        self.chores = GoodChoices(name="chores")
        self.load_chores()

        self.transition = SlideTransition(duration=.25)
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
        with open(self.chores_fn, 'w') as fd:
            json.dump(self.chores.data, fd)

    def del_chore(self, chore_index):
        del self.chores.data[chore_index]
        self.save_chores()
        self.refresh_chores()
        self.go_chores()

    def edit_chore(self, chore_index):
        chore = self.chores.data[chore_index]
        name = 'chore{}'.format(chore_index)

        #not sure what  this check does???
        if self.root.has_screen(name):
            self.root.remove_widget(self.root.get_screen(name)) 

        view = GoodChoicesView(
            name = name,
            chore_index = chore_index,
            chore_description = chore.get('description') 
            )
        
        self.root.add_widget(view) 
        self.transition.direction = 'left' 
        self.root.current = view.name

    def add_chore(self):
        self.chores.data.append({'description': 'New chore (double click)'})
        chore_index = len(self.chores.data) - 1 
        self.edit_chore(chore_index) 

    def set_chore_description(self, chore_index, chore_description):
        self.chores.data[chore_index]['description'] = chore_description 
        self.save_chores() 
        self.refresh_chores() 
    
    def refresh_chores(self):
        data = self.chores.data 
        self.chores.data = []
        self.chores.data = data 

    def go_chores(self):
        self.transition.direction = 'right'
        self.root.current = 'chores' 
    
    @property #adds additional getter and setter functionality to chores_fn()
    def chores_fn(self):
        return join(self.user_data_dir, 'chores.json')
    
    def affirmation(self):
        affirmations = ["Good job!", "Awesome!", "Thank you!", "Keep it up!",
                        "Great work!", "Well done!", "Fabulous!", "Crushing it!"]
        num = randint(0, len(affirmations) - 1)
        self.affirm = affirmations[num]
        return self.affirm
    
    def animate_it(self, instance):
        print(self.root.width)
        print(self.root.height)
        x = randint(0, self.root.width)
        y = randint(0, self.root.height)
        print("x: ", x, "y: ", y)
        animation = Animation(d = 3.0, 
                        pos = (x, y),
                        )

        x = randint(0, self.root.width)
        y = randint(0, self.root.height)
        print("x: ", x, "y: ", y)
        animation += Animation(d=3.0,
                              pos=(x, y),
                              )

        animation += Animation(d = 3.0, 
                        pos = (100, 100), 
                        t = 'out_bounce'
                        )

        
        animation.start(instance)

    def celebrate(self):
        #if self.root.has_screen(name):
            #self.root.remove_widget(self.root.get_screen(name))

        view = CelebrateView()
                     
        self.root.add_widget(view)
        self.transition.direction = 'left'
        self.root.current = view.name
       

if __name__ == "__main__":
    GoodChoicesApp().run()