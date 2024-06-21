from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Welcome to the club, buddy!')  # Создаем кнопку
        btn.border_width = 2
        btn.border_color = (0, 0, 1, 1)  # Цвет бордера (RGBA)
        layout.add_widget(btn)  # Добавляем кнопку поверх изображения
        image = Image(source='E:/Tren_Alex/background_image.jpeg', allow_stretch=True, keep_ratio=False)  # Создаем изображение
        layout.add_widget(image)  # Добавляем изображение в layout

        return layout


if __name__ == '__main__':
    MyApp().run()