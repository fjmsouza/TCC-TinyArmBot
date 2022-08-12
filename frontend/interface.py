from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivy.config import Config

from frontend.screens.ImageScreen import MyBoxLayoutImage
from frontend.screens.VideoScreen import MyBoxLayoutVideo
from frontend.screens.CameraScreen import MyBoxLayoutCamera

Config.set('input', 'mouse', 'mouse,disable_multitouch')


class GerenciaTelas(ScreenManager):
    pass


class Toolbar(Screen):
    pass


class Home(Screen):
    pass


class MyBox(Screen):
    pass


class ImageScreen(MyBoxLayoutImage):
    pass


class VideoScreen(MyBoxLayoutVideo):
    pass


class CameraScreen(MyBoxLayoutCamera):
    pass


class CustomOverFlowMenu(MDDropdownMenu):
    pass


class MainApp(MDApp):
    def build(self):
        self.title = "Ferramenta de Processamento de Imagem"
        return GerenciaTelas()


Window.maximize()
MainApp().run()
