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

class Profile():

    '''Class allows users to add profiles to '''
    
    def __init__(self, first, last, child):
        self.__first = first
        self.__last = last
        self.__child = child
    #Add profile
    #Edit profile

class GoodChoicesChore(Widget):

    '''Class defines the attributes and behaviors associated with all chores'''
    
    def __init__(self, chore, **kwargs):
        super(GoodChoicesChore, self).__init__(**kwargs)
        #print("chore_initialized")
        self.__chore = chore
        #print(self.__chore)
        self.__complete = False
        #print(self.__complete) 
    
    #store a list of chores
    #add a chore
    #edit a chore
    #delete a chore
    #complete a chore- reason for the widget class inheritance
    #reset all chores

class Affirmation(Widget):

    '''Class contains the affirmations for completion and animates them'''

    pass
    #list of affirmations
    #animation

class GoodChoicesLayout(BoxLayout):
    pass

class AffirmationLayout(BoxLayout):
    pass 


class GoodChoicesApp(App):

    def build(self):
        root = GoodChoicesLayout()
        new_chore_list = GoodChoicesChore("dishes")
        root.add_widget(new_chore_list)
        return root
       
if __name__ == "__main__":
    GoodChoicesApp().run()