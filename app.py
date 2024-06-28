from kivy.app import App
from background import MyApp1
from button import MyApp2
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MyApp(MyApp1, MyApp2):
    def build(self):
        super().build()

    def build1(self):
        super().build()


if __name__ == '__main__':
    MyApp().run()
