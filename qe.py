# main.py
from kivy.app import App
from qw import MyClass


class MainApp(App):
    def build(self):
        return MyClass()


if __name__ == '__main__':
    MainApp().run()
