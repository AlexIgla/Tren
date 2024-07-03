from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Button1(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        # создание виджета
        layout = BoxLayout()
        # Добавляем кнопку
        button = Button(text='Welcome to the club, buddy!',
                         size_hint=(.4, .1),
                         pos_hint={'x': .3, 'y': .5})
        button.background_color = (0, 0, 1, 1)  # Устанавливаем синий цвет фона кнопки
        layout.add_widget(button)

        return layout


if __name__ == '__main__':
    Button1().run()
