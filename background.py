from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


def build(self):
    layout = BoxLayout()  # Создаем основной layout
    image = Image(source='E:/Tren_Alex/background_image.jpeg', allow_stretch=True, keep_ratio=False)  # Загружаем изображение
    layout.add_widget(image)  # Добавляем изображение в layout

    return layout
