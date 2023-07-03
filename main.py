'''

Simple application for creating chores and tracking their completion

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation 
from kivy.core.window import Window
from random import random, randint
import time

class Profile():

    '''Profile class allows users to add profiles'''
    
    def __init__(self, first, last, child, **kwargs):
        #super(Profile, self).__init__(**kwargs)
        self.__first = first
        self.__last = last
        self.__child = child

class GoodChoicesChore(Screen):

    '''GoodChoicesChore class defines the attributes and behaviors associated with all chores'''

    # class list for all chores
    chore_dict_list = []
    
    def __init__(self, **kwargs):
        super(GoodChoicesChore, self).__init__(**kwargs)
        print("chore object initialized")
        self.__chore = ''
        self.__complete = False
        self.__index = 0
    
    # add a chore
    def add_chore(self):
        new_chore = self.ids.new_chore.text
        self.__chore = new_chore 
        print("Latest chore", self.__chore)
        chore_dict = {self.__chore : self.__complete}
        GoodChoicesChore.chore_dict_list.append(chore_dict)
        print("Chore List", GoodChoicesChore.chore_dict_list)
        self.__index += 1
        print("Chore Index", self.__index)

class ChoreListScreen(Screen):

    '''Displays the entire list of chores'''

    def view_chore_list(self):
        b = BoxLayout(orientation='vertical',
                      size=(self.width, self.height),
                      padding='10dp'
                      )
        ChoreListScreen.chore_list_items(self, b)
        self.add_widget(b)

    def chore_list_items(self, box):

        key_list = []

        for i in GoodChoicesChore.chore_dict_list:
            for t in i:
                key_list.append(t)

        for i in key_list:
            b = BoxLayout(orientation='horizontal',
                          size=(self.width, self.height)
                          )
            d = Button(text="Delete",
                       size_hint_y=None,
                       size_hint_x=0.2,
                       pos_hint={'center_y' : 0.5}
                       )
            l = Label(text=f'{i}',
                      size_hint_y=None,
                      pos_hint={'center_y': 0.5}
                      )
            t = ToggleButton(
                text="Completed",
                size_hint_y=None,
                pos_hint={'center_y': 0.5}
            )

            t.bind(on_release=self.completed)

            b.add_widget(d)
            b.add_widget(l)
            b.add_widget(t)
            box.add_widget(b)
    
    def completed(self, obj):
        self.manager.current = 'celebrate'

class CelebrateScreen(Screen):

    '''CelebrateScreen class generates the affirmation and animates them when a chore is completed'''

    # generate the affirmation statements
    def affirmation(self):
        affirmations = ["Good job!", "Awesome!", "Thank you!", "Keep it up!",
                        "Great work!", "Well done!", "Fabulous!", "Crushing it!"]
        num = randint(0, len(affirmations) - 1)
        self.affirm = affirmations[num]
        return self.affirm

    #animate the affirmation statement
    def animate_it(self, instance):
        Animation.cancel_all(self)
        print("window width", Window.width)
        print("Self width", self.width)
        print("window height", Window.height)
        print("Self height", self.height)

        random_x = random() * (Window.width)
        #print("random_x #1", random_x)
        random_y = random() * (Window.height)
        #print("random_y #1", random_y)
        anim = Animation(x=random_x, y=random_y, duration=2)

        random_x = random() * (Window.width)
        #print("random_x #2", random_x)
        random_y = random() * (Window.height)
        #print("random_y #2", random_y)
        anim += Animation(x=random_x, y=random_y, duration=2)

        random_x = random() * (Window.width)
        #print("random_x #3", random_x)
        random_y = random() * (Window.height)
        #print("random_y #3", random_y)
        anim += Animation(x=random_x, y=random_y, duration=2)

        anim += Animation(x=0, y=0, duration=2, t="out_elastic")

        anim.start(instance)

class GoodChoicesApp(App):

    '''App class manages the application'''

    def build(self):
        root = ScreenManager()
        root.add_widget(GoodChoicesChore(name='home'))
        root.add_widget(ChoreListScreen(name='chorelistscreen'))
        root.add_widget(CelebrateScreen(name='celebrate'))
        return root 
       
if __name__ == "__main__":
    GoodChoicesApp().run()