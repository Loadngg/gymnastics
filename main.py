from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import exercising as ex
import pyttsx3


Config.set('graphics', 'resizable', False)
Config.set('graphics', 'fullscreen', 1)
tts = pyttsx3.init()
tts.setProperty('voice', 'ru')
tts.setProperty('rate', 225)
tts.setProperty('volume', 1)


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=u'Приложение для Ксюши❤', font_size=30))
        box.add_widget(Button(text='Начать', size_hint=(1, .2), on_press=lambda x: set_screen('main')))
        self.add_widget(box)


class MainScreen(Screen):
    def __init__(self, **kw):
        self.i = 0
        super(MainScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box1 = BoxLayout(orientation='horizontal')
        self.text = ex.exercising_list[self.i]
        exercising = Label(text=self.text, font_size=15)
        box.add_widget(exercising)
        box1.add_widget(Button(text='Предыдущее', size_hint=(1, .2), on_press=lambda x: self.change_ex_prev(exercising)))
        box1.add_widget(Button(text='Следующее', size_hint=(1, .2), on_press=lambda x: self.change_ex_next(exercising)))
        box.add_widget(box1)
        self.add_widget(box)
        # tts.say(self.text)

    def change_ex_next(self, exercising):
        if self.i == 24:
            set_screen('end')
            self.i = 0
        self.i += 1
        self.text = u'{}'.format(ex.exercising_list[self.i])
        exercising.text = self.text
        # if self.text == ex.exercising_list[self.i]:
        #     tts.say(self.text)

    def change_ex_prev(self, exercising):
        if self.i == 0:
            set_screen('menu')
            self.i = 0
        self.i -= 1
        self.text = u'{}'.format(ex.exercising_list[self.i])
        exercising.text = self.text


class EndingScreen(Screen):
    def __init__(self, **kw):
        super(EndingScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text='Поздравляю', font_size=35))
        box.add_widget(Button(text='Закрыть', size_hint=(1, .2), on_press=lambda x: MyApp().stop()))
        self.add_widget(box)


def tts_say(text):
    tts.say(text)
    tts.runAndWait()


def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(EndingScreen(name='end'))


class MyApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyApp().run()
