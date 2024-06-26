from kivy.app import App
from background import MyApp1
from button import MyApp2
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        layout = FloatLayout()
        # Создаем экземпляр класса MyApp1 из файла background
        my_app1_instance = MyApp1()
        my_app1_instance.run()

        # Создаем экземпляр класса MyApp2 из файла button
        my_app2_instance = MyApp2()
        my_app2_instance.run()

        return layout


if __name__ == '__main__':
    MyApp().run()
