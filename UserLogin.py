import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, SlideTransition



kv = Builder.load_string("""
<LoginScreen>:
    
    BoxLayout:
        orientation:'vertical'
        Label:
            text:"username:"
            font_size:"14sp"
            text_size:root.width-20,20
            halign:'left'
        TextInput:
            id: username
            multiline: False
            font_size:"14sp"
        Label:
            text: "password:"
            font_size: "14sp"
            text_size: root.width-20,20
            halign:'left'
        TextInput:
            id: passwd
            multiline: False
            font_size:"14sp"
            password: True
        Button:
            text: "Quit"
            on_release: root.quit()
        Button:
            text: "Login"
            on_release: root.login()
            
<Connected>:
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: "You are now connected"
            font_size: 32
        Button:
            text: "Disconnect"
            font_size: 24
            on_press: root.disconnect()
            on_press: root.login(login.text, password.text)

""")

class LoginScreen(FloatLayout):
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 2

        self.username = TextInput(multiline=False)
        self.password = TextInput(multiline=False, password=True)


class Login(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    Login().run()


class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()