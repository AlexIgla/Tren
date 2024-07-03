from kivy.app import App
from background import Background1
from button import Button1
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout


class MyApp1(Background1, Button1):
    pass


#class MyApp2(Background1, Button1, FloatLayout, App):
#def build(self):
#return MyApp2()


if __name__ == '__main__':
    MyApp1().run()
