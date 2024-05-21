from kivy.app import App
from conexao import connect
from bd import insert, update, delete, query, register, login
from datetime import datetime
from usuario import Usuario
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from functools import partial
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
import os

mydb = connect()

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

class TelaPrincipal(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.inicial_para_login = self.ids.inicial_para_login
        self.inicial_para_login.bind(on_release=partial(self.principal_para_login))

    def principal_para_login(self, instance):
        botao_entrar = Login()
        botao_entrar.open()
        Window.clearcolor = (0, 0, 0, 1)

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()


class Login(FloatLayout):
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
        self.cadastrar_button.bind(on_release=partial(self.check_login))
        self.login_button = self.ids.login_button
        self.login_button.bind(on_release=partial(self.create_new_window))

    def check_login(self, instance):
        nome = self.username_input.get()
        senha = self.senha_input.get()

        user = login(mydb, nome, senha)

        if user:
            print("Login bem-sucedido!")
            telainicial = TelaInicial()
            telainicial.open()
        else:
            print("Credenciais inválidas!")
            return None

    def create_new_window(self, instance):
        new_window = NewWindow()
        new_window.open()
        Window.clearcolor = (0, 0, 0, 1)  # Mudar a cor de fundo para preto

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class NewWindow(FloatLayout):
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
        self.button_cadastrar.bind(on_release=partial(self.register_user))
        self.botao_login = self.ids.botao_login
        self.botao_login.bind(on_release=partial(self.botao_voltar_login))

    def botao_voltar_login(self, instance):
        voltar_login = Login()
        voltar_login.open()

    def register_user(self, instance):
        user_data = {
            'nome': self.username_input.get(),
            'email': self.email_input.get(),
            'celular': self.celular_input.get(),
            'senha': self.senha_input.get()
        }
        register(mydb, user_data['nome'], user_data['email'], user_data['celular'], user_data['senha'])

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class TelaInicial(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado

        self.botao_ocorrencia = self.ids.botao_ocorrencia
        self.botao_ocorrencia.bind(on_release=partial(self.funcao_entrar_ocorrencia))
        self.minha_denuncia = self.ids.minha_denuncia
        self.minha_denuncia.bind(on_release=partial(self.entrar_minha_ocorrencia))
        self.denuncia_outra_pessoa = self.ids.denuncia_outra_pessoa
        self.denuncia_outra_pessoa.bind(on_release=partial(self.abrir_nova_ocorrencia))

    def funcao_entrar_ocorrencia(self, instance):
        func_ocorrencia = Ocorrencia()
        func_ocorrencia.open()

    def abrir_nova_ocorrencia(self, instance):
        abrir_ocorrencia = AbrirOcorrencia()
        abrir_ocorrencia.open()

    def entrar_minha_ocorrencia(self, instance):
        minha_ocorrencia = ListaOcorrencias()
        minha_ocorrencia.open()
        Window.clearcolor = (0, 0, 0, 1)

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()
    
class ListaOcorrencias(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  
        self.arg2 = None  

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.lista_ocorrencia = self.ids.lista_ocorrencia
        self.lista_ocorrencia.bind(on_release=partial(self.abrir_lista_assalto))
        self.lista_assedio = self.ids.lista_assedio
        self.lista_assedio.bind(on_release=partial(self.abrir_lista_assedio))
        self.voltar_telainicial = self.ids.voltar_telainicial
        self.voltar_telainicial.bind(on_release=partial(self.voltar_para_telainicial))

    def abrir_lista_assedio(self, instance):
        lista_assedio = ListaDenunciaAssedio()
        lista_assedio.open()

    def abrir_lista_assalto(self, instance):
        lista_assaltos = ListaDenunciaAssalto()
        lista_assaltos.open()

    def voltar_para_telainicial(self, instance):
        telainicial_voltar = TelaInicial()
        telainicial_voltar.open()
        Window.clearcolor = (0, 0, 0, 1)

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class AbrirOcorrencia(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  
        self.arg2 = None  

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.nome_completo = self.ids.nome_completo
        self.cpf = self.ids.cpf
        self.data_nascimento = self.ids.data_nascimento
        self.email = self.ids.email
        self.voltarparatelainicial = self.ids.voltarparatelainicial
        self.voltarparatelainicial.bind(on_release=partial(self.voltar_para_tela_inicial))
        self.ocorrencia_prox = self.ids.ocorrencia_prox
        self.botao_enviar_ocorrencia = self.ids.botao_enviar_ocorrencia
        self.endereço_amigo = self.ids.endereco_amigo
        self.reference = self.ids.reference

    def voltar_para_tela_inicial(self, instance):
        icone_casa = TelaInicial()
        icone_casa.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()


class Ocorrencia(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.enviar_ocorrencia_botao = self.ids.enviar_ocorrencia_botao
        self.seta_voltar = self.ids.seta_voltar
        self.seta_voltar.bind(on_release=partial(self.apertar_voltar))
        self.nomeseu_completo = self.ids.nomeseu_completo
        self.seucpf = self.ids.seucpf
        self.suadata_nasc = self.ids.suadata_nasc
        self.seuemail = self.ids.seuemail
        self.seuendereco = self.ids.seuendereco
        self.suareferencia = self.ids.suareferencia
        self.suadescricao = self.ids.suadescricao

    def apertar_voltar(self, instance):
        voltar_casinha = TelaInicial()
        voltar_casinha.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class ListaDenunciaAssalto(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.listar_assalto = self.ids.listar_assalto
        self.setinha = self.ids.setinha
        self.setinha.bind(on_release=partial(self.setinha_voltar))

    def setinha_voltar(self, instance):
        setinha = ListaOcorrencias()
        setinha.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class ListaDenunciaAssedio(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.listar_assedio = self.ids.listar_assedio
        self.miniseta = self.ids.miniseta
        self.miniseta.bind(on_release=partial(self.miniseta_voltar))

    def miniseta_voltar(self, instance):
        volte = ListaOcorrencias()
        volte.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class MyApp(App):
    def build(self):
        return TelaPrincipal()
        
if __name__ == '__main__':
    MyApp().run()


mydb.close()



