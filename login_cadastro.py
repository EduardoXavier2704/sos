from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from functools import partial
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
import os

# Obter o caminho absoluto do diretório onde o script está localizado
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto para o arquivo KV
kv_file = os.path.join(current_dir, 'login_cadastro.kv')

# Verificar se o arquivo KV existe
if not os.path.exists(kv_file):
    print(f"Arquivo KV não encontrado: {kv_file}")
    raise FileNotFoundError(f"Arquivo KV não encontrado: {kv_file}")

# Carregar o arquivo KV
Builder.load_file(kv_file)

class Login(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.username_input = self.ids.username_input
        self.senha_input = self.ids.senha_input

        self.cadastrar_button = self.ids.cadastrar_button
        self.cadastrar_button.bind(on_release=partial(self.create_new_telainicial))
        self.login_button = self.ids.login_button
        self.login_button.bind(on_release=partial(self.create_new_window))

    def create_new_telainicial(self, instance):
        telainicial = TelaInicial()
        telainicial.open()
        Window.clearcolor = (0, 0, 0, 1)

    def create_new_window(self, instance):
        new_window = NewWindow()
        new_window.open()
        Window.clearcolor = (0, 0, 0, 1)  # Mudar a cor de fundo para preto

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class NewWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 1)  # Mudar a cor de fundo para preto

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.username_input = self.ids.username_input
        self.email_input = self.ids.email_input
        self.celular_input = self.ids.celular_input
        self.senha_input = self.ids.senha_input

        self.button_cadastrar = self.ids.button_cadastrar
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login))

    def entrar_interface_login(self, instance):
        entrar_login = Login()
        entrar_login.open()
        Window.clearcolor = (0, 0, 0, 1)  # Mudar a cor de fundo para preto

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class TelaInicial(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado

        self.botao_ocorrencia = self.ids.botao_ocorrencia
        self.minha_denuncia = self.ids.minha_denuncia
        self.emergencia = self.ids.emergencia
        self.denuncia_outra_pessoa = self.ids.denuncia_outra_pessoa

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()


