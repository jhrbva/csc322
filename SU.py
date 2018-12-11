from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

#for matching
import re


userName = 'Rong'
#for tabo usage
suggestTaboList = ['1','2','3','2','3','2','3','2','3']
taboList = ['physics', 'chemistry', '1997', '2000',"a", "b", "c", "d"]
selectedTabo=[]

def renewtabo(TL,STL):
    taboList.clear()
    for item in TL:taboList.append(item)
    suggestTaboList.clear()
    for item in STL:suggestTaboList.append(item)
    print(suggestTaboList)
    selectedTabo.clear()


#for tabo usage
class MyTaboButton(Button):

    def select(self):
        self.selected = not self.selected

        try:
            selectedTabo.index(self.text)
            selectedTabo.remove(self.text)
        except ValueError:
            selectedTabo.append(self.text)
        print(selectedTabo)
    pass





class FileLabel(BoxLayout):

    def testC(self):
        print(self.data)
        print("hi")
    pass



class Test(BoxLayout):

    def doubleclick(self,but,touch):
        if touch.is_double_tap:
            print("hi")

    def hi(self):
        print("hi")

    def changeUserName(self):
        self.userNameLabel.text = userName

    def populate(self):
        self.fileList.data = [{'user':''.join(sample(ascii_lowercase, 6)),'title': '1','author': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]
    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])
    def clear(self):
        self.rv.data = []
    def insert(self, value):
        self.rv.data.insert(0, {'value': value or 'default value'})
    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()
    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)


    def setRV(self):
        self.rv1.data = [{'user':'wtf','title':'i dont know','author':'wentom'}]
        self.rv1.refresh_from_data()



    #taboo list funciton
    def taboInit(self):
        self.taboL.data = [{ 'data': item} for item in taboList]
        self.sugTaboL.data = [{ 'data': item} for item in suggestTaboList]
    
    def removeTabo(self):
        if(len(selectedTabo)>0):
            ntaboList = [elem for elem in taboList if elem not in selectedTabo]
            nsuggestTaboList = [elem for elem in suggestTaboList if elem not in selectedTabo]
            self.taboL.data = [{ 'data': item,'selected':False} for item in ntaboList]
            self.sugTaboL.data = [{ 'data': item,'selected':False} for item in nsuggestTaboList]
            renewtabo(ntaboList,nsuggestTaboList)  

    def acceptTabo(self):
        if(len(selectedTabo)>0):
            ntaboList = [elem for elem in taboList if elem not in selectedTabo] + selectedTabo
            nsuggestTaboList = [elem for elem in suggestTaboList if elem not in selectedTabo]
            self.taboL.data = [{ 'data': item,'selected':False} for item in ntaboList]
            self.sugTaboL.data = [{ 'data': item,'selected':False} for item in nsuggestTaboList]
            renewtabo(ntaboList,nsuggestTaboList)

    def addTabo(self):
        if(self.ids['addTaboTI'].text):
            tmp =self.ids['addTaboTI'].text
            if(tmp not in taboList):
                taboList.append(tmp)
                self.taboL.data = [{ 'data': item,'selected':False} for item in taboList]

    def searchTaboL(self):
        tmp = self.ids['searchTaboTI'].text
        tmpt = []
        tmps = []
        print(tmp)
        print(tmpt)
        print(tmps)
        if tmp :
            for item in taboList: 
                if re.match(tmp,item):
                    tmpt.append(item)
            for item in suggestTaboList: 
                if re.match(tmp,item):
                    tmps.append(item)
            self.taboL.data = [{ 'data': item,'selected':False} for item in tmpt]
            self.sugTaboL.data = [{ 'data': item,'selected':False} for item in tmps]

        else:
            self.taboL.data = [{ 'data': item,'selected':False} for item in taboList]
            self.sugTaboL.data = [{ 'data': item,'selected':False} for item in suggestTaboList]
        


class TestApp(App):
    def build(self):
        self.load_kv('SU.kv')
        return Test()



if __name__ == '__main__':

    TestApp().run()