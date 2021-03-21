import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
import exercising as ex

kivy.require('2.0.0')


class MenuScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kw):
        self.i = 0
        super(MainScreen, self).__init__(**kw)
        self.text = ex.exercising_list[self.i]

    def change_ex_next(self, exercising):
        if self.i == 24:
            self.i = 0
        self.i += 1
        self.text = u'{}'.format(ex.exercising_list[self.i])
        exercising.text = self.text

    def change_ex_prev(self, exercising):
        if self.i == 0:
            pass
        self.i -= 1
        self.text = u'{}'.format(ex.exercising_list[self.i])
        exercising.text = self.text


class EndingScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1920, 1080)
        Window.fullscreen = True


if __name__ == "__main__":
    MyApp().run()
