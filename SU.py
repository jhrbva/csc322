from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import datetime
import file 
import Membership
import csv
import user

my_file = file.File(0, "", "", datetime.date.today(),'public',[],[""],False)
my_file.file_information()

my_mem = Membership.Membership(['l','i','a','d','e','f'],['i','f','yoo','ok'],['123','34543','789'],'admin')

#for matching
import re

userName = 'Rong'

my_user = user.User(999,'guest','guest','guest',[])


tmp_file = file.File(0, "", "", datetime.date.today(),'public',[],[""],False)

# usage for file choice
class FileListL(GridLayout):

    def openFile(self,but,touch):
        if touch.is_double_tap:
            k = self.fileid
            print("new open")
            print(self.fileid)
            self.openf(k)
    def openf(self,id):
        with open('csvexample.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                if row['id'] == id:
                    my_file.update(row['id'],row['title'],row['author'],row['date'],row['visibility'],row['friend_list'],row['history'],row['locked'])
                    print([row['id'],row['title'],row['author'],row['date'],row['visibility'],row['friend_list'],row['history'],row['locked']])


#edit file

class membership(Screen):
    def addOu(self):
        print("hi")




#for tabo usage
suggestTaboList = ['1','2','3','2','3','2','3','2','3']
taboList = ['physics',  'chemistry', '1997', '2000',"a", "b", "c", "d"]
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

class MyMemButton(Button):

    def select(self):
        self.selected = not self.selected
        my_mem.addsSelected(self.text)


class FileLabel(BoxLayout):

    def testC(self):
        print(self.data)
        print("hi")
    pass


class Test(GridLayout):


    def login(self):
        found = False
    #assume that you are looking for user ID = 188
        with open('userdatabase.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                print(row)
                if row['username'] == self.ids['username'].text:
                    found = True
                    if row['pwd'] == self.ids['passwd'].text:
                        my_user.update(row['id'],row['type'],row['username'],row['pwd'],row['filesvisited'])
                        print("login")
                        self.ids['mainManager'].current= 'SU'
                        self.initglobaluser()
                        self.setFileListRV()
                        self.initEfile()
                    else:
                        self.ids['logininfo'].text = "Incorrect Password"
        if not found:  
            self.ids['logininfo'].text = "No such user"


    def initglobaluser(self):
        self.ids['userNameLabel'].text = my_user.username
        if my_user.user_type== 'guest':
            self.guest = True

    def setFileListRV(self):
        self.ids['fileListRv'].data = [{'fileid':f,'title':t,'author':a,'visibility':v} for f,t,a,v in my_file.read_file() ]
        print(self.ids['fileListRv'].data)
        self.ids['fileListRv'].refresh_from_data()

    def initEfile(self):
        if my_user.user_type== 'guest':
            self.guest = True
        self.ids['fileAuthor'].text = my_file.title
        self.ids['filelock'].text = 'Lock' if my_file.locked else 'Unlock'
        self.ids['friendList'].data = [{ 'text': item} for item in my_file.friend_list]
        self.ids['fileVer'].text = str(my_file.currenth)
        self.ids['filetext'].text = my_file.text

    def saveH(self):
        if my_user.user_type!='guest':
            my_file.save()
            self.ids['fileVer'].text = str(my_file.currenth)

    def changetext(self):
        if my_user.user_type!='guest':
            my_file.text_update(self.ids['filetext'].text)
        print(my_file.text)

    def changeV(self,way):
        my_file.version_history(way)
        self.ids['filetext'].text = my_file.text
        self.ids['fileVer'].text = str(my_file.currenth)

    #file list function??

    def updateoptionChoic(self,go):
        if my_user.user_type != 'guest':
            self.ids['optionChoic'].current = go

    #taboo list funciton-----------------------
    def taboInit(self):
        self.taboL.data = [{ 'data': item} for item in taboList]
        self.sugTaboL.data = [{ 'data': item} for item in suggestTaboList]
    
    def removeTabo(self):
        if(len(selectedTabo)>0):
            if my_user.user_type!='guest':
                ntaboList = [elem for elem in taboList if elem not in selectedTabo]
            else:
                ntaboList= taboList
            nsuggestTaboList = [elem for elem in suggestTaboList if elem not in selectedTabo]
            self.taboL.data = [{ 'data': item,'selected':False} for item in ntaboList]
            self.sugTaboL.data = [{ 'data': item,'selected':False} for item in nsuggestTaboList]
            renewtabo(ntaboList,nsuggestTaboList)  

    def acceptTabo(self):
        if my_user.user_type!='guest':
            if(len(selectedTabo)>0):
                ntaboList = [elem for elem in taboList if elem not in selectedTabo] + selectedTabo
                nsuggestTaboList = [elem for elem in suggestTaboList if elem not in selectedTabo]
                self.taboL.data = [{ 'data': item,'selected':False} for item in ntaboList]
                self.sugTaboL.data = [{ 'data': item,'selected':False} for item in nsuggestTaboList]
                renewtabo(ntaboList,nsuggestTaboList)

    def addTabo(self):

        if my_user.user_type!='guest':
            if(self.ids['addTaboTI'].text):
                tmp =self.ids['addTaboTI'].text
                if(tmp not in taboList):
                    taboList.append(tmp)
                    self.taboL.data = [{ 'data': item,'selected':False} for item in taboList]
        else:
            if(self.ids['addTaboTI'].text):
                tmp =self.ids['addTaboTI'].text
                if(tmp not in suggestTaboList):
                    suggestTaboList.append(tmp)
                    self.sugTaboL.data = [{ 'data': item,'selected':False} for item in suggestTaboList]

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
        
    #mem function
    def meminit(self):
        self.ids['SUL'].data= [{ 'data': item,'selected':False} for item in my_mem.SUL]
        self.ids['OUL'].data= [{ 'data': item,'selected':False} for item in my_mem.OU]
        self.ids['APL'].data= [{ 'data': item,'selected':False} for item in my_mem.APL]
    
    def addOU(self):
        my_mem.addOU(self.ids['addOU'].text)
        self.ids['OUL'].data= [{ 'data': item,'selected':False} for item in my_mem.OU]

    def promote(self):
        my_mem.accept()
        self.meminit()

    def memRemove(self):
        my_mem.remove()
        self.meminit()
    
    def searchM(self):
        tmp = self.ids['searchMem'].text
        tmpa = []
        tmpb = []
        tmpc = []
        if tmp :
            for item in my_mem.SUL: 
                if re.match(tmp,item):
                    tmpa.append(item)
            for item in my_mem.OU: 
                if re.match(tmp,item):
                    tmpb.append(item)
            for item in my_mem.APL: 
                if re.match(tmp,item):
                    tmpc.append(item)
            self.ids['SUL'].data= [{ 'data': item,'selected':False} for item in tmpa]
            self.ids['OUL'].data= [{ 'data': item,'selected':False} for item in tmpb]
            self.ids['APL'].data= [{ 'data': item,'selected':False} for item in tmpc]
        else:
            self.meminit()
    #-----------------    

class TestApp(App):
    def build(self):
        self.load_kv('editfileScreen.kv')
        self.load_kv('SU.kv')
        return Test()



if __name__ == '__main__':

    TestApp().run()