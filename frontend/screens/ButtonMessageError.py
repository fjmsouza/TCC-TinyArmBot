from kivy.uix.behaviors.button import ButtonBehavior
from kivy.properties import ListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class ButtonError(ButtonBehavior, Label):
    cor = ListProperty([0.1, 0.5, 0.7, 1])
    cor2 = ListProperty([0.1, 0.1, 0.1, 1])

    def __init__(self, **kwargs):
        super(ButtonError, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_release(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_cor(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height), pos=self.pos)
            Ellipse(size=(self.height, self.height), pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height), pos=(self.x + self.height / 2.0, self.y))

    @staticmethod
    def message_error(valor):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        botoes = BoxLayout(orientation='vertical', padding=10, spacing=10)
        pop = Popup(title="Atenção!", title_size=32, title_align='center', content=box, size_hint=(None, None),
                    size=(400, 240))
        label = Label(text=valor, font_size=24)
        ok = ButtonError(text='OK', on_release=pop.dismiss)
        botoes.add_widget(label)
        botoes.add_widget(ok)
        box.add_widget(botoes)
        pop.open()
