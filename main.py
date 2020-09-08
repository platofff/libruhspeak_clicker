import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('controller.kv')


class MenuScreen(Screen):
    pass


class ClickerScreen(Screen):
    pass


class Application(App):
    _score = 0
    _character: str

    def clicker(self, character: str):
        self._character = character
        self._clicker.ids.image.background_normal = f'./images/{character}1.jpg'
        self._sm.current = 'clicker'

    def _click(self):
        self._score += 1
        if self._score % 100:
            newImage = f'./images/{self._character}{int(self._score / 100) + 1}.jpg'
            if os.path.exists(newImage):
                self._clicker.ids.image.background_normal = f'./images/{self._character}{int(self._score / 100) + 1}.jpg'
        self._clicker.ids.score.text = str(self._score)

    def __init__(self):
        super().__init__()
        self._clicker = ClickerScreen(name='clicker')
        self._sm = ScreenManager()
        self._sm.add_widget(MenuScreen(name='menu'))
        self._sm.add_widget(self._clicker)

    def build(self):
        return self._sm


if __name__ == '__main__':
    Application().run()
