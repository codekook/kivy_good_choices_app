'''

Simple application for creating chores and tracking their completion

Design challenges and bugs-
- Formatting the entire list of chores to display correctly
- Keeping the animation to the window size 
- Deleting chores in the list
- Prevent mulitple "View Chores" function calls on top of one another 

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

    '''GoodChoicesChore class instantiates, adds, and deletes chores from a list of dictionaries'''

    # class list for all chores
    chore_dict_list = []
    
    def __init__(self, **kwargs):
        super(GoodChoicesChore, self).__init__(**kwargs)
        print("chore object initialized")
        self.__chore = ''
        self.__complete = False
        self.__index = 0
    
    # adds a chore
    def add_chore(self):
        new_chore = self.ids.new_chore.text
        self.__chore = new_chore 
        print("Latest chore", self.__chore)
        chore_dict = {self.__chore : self.__complete}
        GoodChoicesChore.chore_dict_list.append(chore_dict)
        print("Chore List", GoodChoicesChore.chore_dict_list)
        self.__index += 1
        print("Chore Index", self.__index)
    
    # delete a chore
    def delete_chore(self):
        pass

class ChoreListScreen(Screen):

    '''Displays the entire list of chores and whether they are completed or not'''

    # creates all the buttons on the screen and displays each chore
    def view_chore_list(self):
        key_list = []

        box_layout = BoxLayout(orientation='vertical',
                      size=(self.width, self.height),
                      padding='5dp'
                    )
        home_button = Button(text='Home',
                    size_hint_y=None,
                    pos_hint={'top': 1}
                    )

        box_layout.add_widget(home_button)
        home_button.bind(on_press=self.shift_to_home)

        for i in GoodChoicesChore.chore_dict_list:
            for t in i:
                key_list.append(t)

        for i in key_list:
            chore_box = BoxLayout(orientation='horizontal',
                          size=(self.width, self.height)
                          )
            del_button = Button(text="Delete",
                       size_hint_y=None,
                       size_hint_x=0.5,
                       pos_hint={'center_y': 0.1}
                       )
            label = Label(text=f'{i}',
                      size_hint_y=None,
                      pos_hint={'center_y': 0.1}
                      )
            toggle_b = ToggleButton(
                text="Completed",
                size_hint_y=None,
                pos_hint={'center_y': 0.1}
            )
            #print("state before: ", toggle_b.state)

            toggle_b.bind(on_release=self.completed)
            del_button.bind(on_release=self.delete_chore)

            chore_box.add_widget(del_button)
            chore_box.add_widget(label)
            chore_box.add_widget(toggle_b)
            box_layout.add_widget(chore_box)

        self.add_widget(box_layout)
    
    # changes the state of the togglebutton and switches to the celebrate screen
    def completed(self, obj):
        #print("state before: ", obj.state)
        if obj.state == "down":
            self.manager.current = "celebrate"
    
    # shifts the screen back to home
    def shift_to_home(self, obj):
        self.manager.current = "home"
    
    # removes the chore from the key_list and calls the delete function from GoodChoicesChore class 
    def delete_chore(self, obj):
        pass 

class CelebrateScreen(Screen):

    '''CelebrateScreen class generates the affirmation and animates them when a chore is completed'''

    # generate the affirmation statements
    def affirmation(self):
        affirmations = ["Good job!", "Awesome!", "Thank you!", "Keep it up!",
                        "Great work!", "Well done!", "Fabulous!", "Crushing it!"]
        num = randint(0, len(affirmations) - 1)
        self.affirm = affirmations[num]
        return self.affirm

    # animates the affirmation statement
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