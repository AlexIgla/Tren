from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class Background1(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        # создание виджета с вертикальной ориентацией
        layout = BoxLayout(orientation='vertical')
        # создание изображения
        image = Image(source='E:/Tren_Alex/background_image.jpeg',
                      allow_stretch=True,
                      keep_ratio=False)
        # добавление изображения в layout
        layout.add_widget(image)

        return layout


if __name__ == '__main__':
    Background1().run()
