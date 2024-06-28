# my_class.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyClass(App):
    def __init__(self, button, background_color, **kwargs):
        # создание виджета
        super().__init__(**kwargs)
        layout = BoxLayout()
        # Добавляем кнопку
        self.button = button(text='Welcome to the club, buddy!',
                             size_hint=(.4, .1),
                             pos_hint={'x': .3, 'y': .5})
        # Устанавливаем синий цвет фона кнопки
        self.background_color = background_color(0, 0, 1, 1)
        layout.add_widget(button)

        return layout
