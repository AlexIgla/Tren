from kivy.app import App
from background import Background1
from button import Button1
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout


class MyApp1(Button1, Background1, FloatLayout, App):
    pass


if __name__ == '__main__':
    MyApp1().run()
