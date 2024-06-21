from kivy.lang import Builder
from kivy.app import App

KV = """
MDScreen:

    FloatLayout:

        Image:
            source: 'E:/Tren_Alex/background_image.jpeg'  # Укажите путь к вашему изображению здесь
            allow_stretch: True
            keep_ratio: 0

        MDRaisedButton:
            text: "Нажми меня"
            pos_hint: {"center_x":.5, "center_y":.5}
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()
