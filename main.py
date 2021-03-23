import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import exercising as ex
import pyttsx3

kivy.require('2.0.0')

tts = pyttsx3.init()
tts.setProperty('rate', 250)
tts.setProperty('volume', 1)


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
            sm.current = 'end'
        self.i += 1
        self.text = u'{}'.format(ex.exercising_list[self.i])
        exercising.text = self.text

    def change_ex_prev(self, exercising):
        if self.i == 0:
            sm.current = 'menu'
        self.i -= 1
        self.text = u'{}'.format(ex.exercising_list[self.i])
        exercising.text = self.text


class EndingScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(EndingScreen(name='end'))

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1920, 1080)
        Window.fullscreen = True

        return sm


if __name__ == "__main__":
    MyApp().run()
