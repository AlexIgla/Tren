from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line, Color
from kivy.clock import Clock


class MyButton(Button):
    def __init__(self,**kw):
        super().__init__(**kw)
        self.text = 'test'
        Clock.schedule_once(self.update_border,1)

    def update_border(self,dt):
        with self.canvas.before:
            Color(rgba = (1,1,1,1))
            Line(width = 2,rectangle = (self.x,self.y,self.width,self.height))

class Main(BoxLayout):
    def __init__(self,**kw):
        super().__init__(**kw)
        self.orientation = 'vertical'
        self.add_widget(Widget())
        self.add_widget(MyButton())
        self.add_widget(Widget())


class MyApp(App):
    def build(self):
        return Main()

if __name__ == "__main__":
    MyApp().run()