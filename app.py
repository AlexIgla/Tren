from kivy.app import App
from background import build
from button import button


class MyApp(App):
    def __init__(self):
        super().__init__()  # Вызов метода __init__ суперкласса
        self.build()  # Создание ссылки на функцию из другого файла
        self.button()  # Создание ссылки на функцию из другого файла

    def build(self):
        return build(self)

    def button(self):
        return button(self)


my_object = MyApp()  # Создание экземпляра класса

my_object.run()  # Запуск приложения
