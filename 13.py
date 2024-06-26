from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class MyApp(App):
    def build(self):
        # Создаем кнопку
        button = Button(text='Hello, Kivy!', size_hint=(None, None), size=(200, 50))

        # Создаем прямоугольник для фона
        with button.canvas.before:
            Color(1, 1, 1, 1)  # Цвет фона (RGBA)
            Rectangle(pos=button.pos, size=button.size)

        return button


if __name__ == '__main__':
    MyApp().run()
