'''

Simple application for creating chores and tracking their completion

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation 
from random import randint

class Profile():

    '''Class allows users to add profiles to '''
    
    def __init__(self, first, last, child, **kwargs):
        #super(Profile, self).__init__(**kwargs)
        self.__first = first
        self.__last = last
        self.__child = child
    #Add profile
    #Edit profile

class GoodChoicesChore(Widget):

    '''Class defines the attributes and behaviors associated with all chores'''

    #class list for all chores
    chore_dict_list = []
    
    def __init__(self, **kwargs):
        super(GoodChoicesChore, self).__init__(**kwargs)
        #print("chore_initialized")
        self.__chore = ''
        #print(self.__chore)
        self.__complete = False
        #print(self.__complete)
        self.__index = 0
        #print(self.__index)
    
    # returns the self.__chore object as a string
    #def __str__(self):
        #return f'GoodChoicesChore({self.__chore})'
    
    #add a chore
    def add_chore(self):
        new_chore = self.ids.new_chore.text
        self.__chore = new_chore 
        print(self.__chore)
        chore_dict = {self.__chore : self.__complete}
        GoodChoicesChore.chore_dict_list.append(chore_dict)
        print(GoodChoicesChore.chore_dict_list)

    def add_chore_list_item(self):
        b = BoxLayout(orientation='vertical', size=(self.width, self.height))
        l = Label(text=self.__chore, size_hint_y=None, pos_hint={'top': 1})
        t = ToggleButton(text="Completed", size_hint_y=None, pos_hint={'top' : 1})
        b.add_widget(l)
        b.add_widget(t)
        self.add_widget(b)

    #edit a chore
    #delete a chore
    #complete a chore- reason for the widget class inheritance
    #reset all chores

class Affirmation(Widget):

    '''Class contains the affirmations for completion and animates them'''

    pass
    #list of affirmations
    #animation

class GoodChoicesApp(App):

    def build(self):
        root = GoodChoicesChore()
        return root
       
if __name__ == "__main__":
    GoodChoicesApp().run()