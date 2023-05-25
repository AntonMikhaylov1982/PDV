from kivy.app import App
from kivy.uix.label import Label

#from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
#from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
#from kivy.properties import ListProperty

#import locale
#import gettext
#
import os
from os.path import dirname, join

#locale.setlocale(locale.LC_ALL, 'deu_deu')

class Widget(App):
    def build(self):
        label = Label(text = 'NEON ПДВ 1.45',
                      size_hint = (1,1),
                      pos_hint = {'center_x':0.07,'center_y':0.98}
                      )
        return label


if __name__ == "__main__":
    window = Widget().run()


