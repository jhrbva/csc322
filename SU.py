from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
import file

my_file = file.File(123, "My File", "Julia", datetime.date.today(),2,["Yannis",'sdsa','asdsadsa'],["This is the text in my file","2","3","4"],True)
my_file.file_information()

#for matching
import re

userName = 'Rong'




# usage for file choice
class FileListL(GridLayout):

    def openFile(self,but,touch):
        if touch.is_double_tap:
            print("hi")

#edit file
class EditFIleScreen(Screen):
    def ok(self):
        print(self.ids['fileAuthor'].text)
        print(my_file.file_information())
        self.ids['fileAuthor'].text = my_file.title
        self.ids['filelock'].text = 'Lock' if my_file.lock else 'Unlock'
        self.ids['friendList'].data = [{ 'text': item} for item in my_file.friend_list]
        self.ids['fileVer'].text = str(my_file.history)

    def changetext(self):
        my_file.text_update(self.ids['filetext'].text)



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

    #file list function??

    def setFileListRV(self):
        self.ids['fileListRv'].data = [{'visibility':'wtf','title':'i dont know','author':'wentom'}]
        print(self.ids['fileListRv'].data)
        self.ids['fileListRv'].refresh_from_data()


    #taboo list funciton-----------------------
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
    #tabo -------------------------------
        


class TestApp(App):
    def build(self):
        self.load_kv('editfileScreen.kv')
        self.load_kv('SU.kv')
        return Test()



if __name__ == '__main__':

    TestApp().run()