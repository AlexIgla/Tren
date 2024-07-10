from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class RootWidget(FloatLayout):
    pass


class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)


class MainApp(App):
    def build(self):
        root = RootWidget()
        c = CustomLayout()
        root.add_widget(c)
        c.add_widget(
            Image(
                source="E:/Tren_Alex/background_image.jpeg",
                allow_stretch=True,
                keep_ratio=False))
        c = CustomLayout()
        c.add_widget(
            Button(text='Welcome to the club, buddy!',
                   size_hint=(.5, .1),
                   pos_hint={'center_x': .5, 'center_y': .5},
                   background_color='blue'))
        root.add_widget(c)
        return root