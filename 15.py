from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class MyApp1(App):
    def build(self):
        layout = FloatLayout()

        # Добавляем изображение
        image = Image(source='E:/Tren_Alex/background_image.jpeg',
                      allow_stretch=True,
                      keep_ratio=False)
        layout.add_widget(image)

        # Добавляем кнопку
        button = Button(text='Welcome to the club, buddy!',
                        size_hint=(.4, .1),
                        pos_hint={'x': .3, 'y': .5})
        button.background_color = (0, 0, 1, 1)  # Устанавливаем синий цвет фона кнопки
        layout.add_widget(button)

        return layout


class MyApp(MyApp1):
    def build(self):
        super().build()
        return None


if __name__ == '__main__':
    MyApp().run()