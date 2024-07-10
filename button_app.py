from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        # Добавляем виджет
        layout = FloatLayout()
        # Добавляем изображение
        image = Image(source='E:/Tren_Alex/background_image.jpeg',
                      allow_stretch=True,
                      keep_ratio=False)
        layout.add_widget(image)
        # Добавляем кнопку
        button = Button(text='Welcome to the club, buddy!',
                        size_hint=(.5, .1),
                        pos_hint={'center_x': .5, 'center_y': .5})
        # Добавляем цвет кнопке
        button.background_color = 'blue'
        layout.add_widget(button)

        return layout
