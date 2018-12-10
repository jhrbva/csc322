import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, SlideTransition


kv = Builder.load_string("""
<Button>:
    font_size: 20
    color: 0,1,0,1
    size_hint: 0.1, 0.1
    
<Label>:
    font_size: 20
    color: 0,1,0,1
    size_hint: 0.1, 0.1 
    
<TextInput>:
    font_size: 20
    color: 0,1,0,1
    size_hint: 0.4, 0.1 
    
<LoginScreen>:
    rows: 3
    FloatLayout:
        Label:
            pos_hint: {"x": .2, 'y':.65}
            height:dp(36)
            text: "username:"
            font_size:"14sp"
            halign:'left'
        TextInput:
            pos_hint: {"x": .3, 'y':.65}
            height:dp(36)
            id: username
            multiline: False
            font_size:"14sp"
        
            
        Label:
            pos_hint: {"x": .2, 'y':.55}
            text: "password:"
            font_size: "14sp"
            halign:'left'
        TextInput:
            pos_hint: {"x": .3, 'y':.55}
            id: passwd
            multiline: False
            font_size:"14sp"
            password: True
        Button:
            pos_hint: {"x": .4, 'y':.45}
            text: "Quit"
            on_release: root.quit()
        Button:
            pos_hint: {"x": .5, 'y':.45}
            text: "Login"
            on_release: root.login()
                

""")


class LoginScreen(FloatLayout):
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)

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