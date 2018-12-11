from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


userName = 'Yannis'


class FileLabel(BoxLayout):

    def testC(self):
        print(self.data)
        print("hi")
    pass


class Test(BoxLayout):

    def doubleclick(self, but, touch):
        if touch.is_double_tap:
            print("hi")

    def hi(self):
        print("hi")

    def changeUserName(self):
        self.userNameLabel.text = userName

    def populate(self):
        self.fileList.data = [{'user':''.join(sample(ascii_lowercase, 6)), 'title': ''.join(sample(ascii_lowercase, 6)), 'author': ''.join(sample(ascii_lowercase, 6))}
                              for x in range(50)]

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def setRV(self):
        self.rv1.data = [{'user': 'wtf', 'title': 'i dont know', 'author': 'wentom'}]
        self.rv1.refresh_from_data()


class TestApp(App):
    def build(self):
        self.load_kv('GU.kv')
        return Test()


if __name__ == '__main__':
    TestApp().run()