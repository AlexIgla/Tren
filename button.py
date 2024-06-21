from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def button(self):
    layout = BoxLayout()
    btn = Button(text='Hello, Kivy!')  # Создаем кнопку
    btn.border_width = 2
    btn.border_color = (0, 0, 1, 1)  # Цвет бордера (RGBA)
    layout.add_widget(btn)  # Добавляем кнопку в layout

    return layout
