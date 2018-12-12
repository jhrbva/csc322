import datetime
import csv
import ast

class File:

    #class attribute
    file_visibility = ['private', 'shared', 'public']
    
    # initializer
    def __init__(self, file_id, title, author, date, visibility, friend_list, history, locked):
        self.file_id = file_id
        self.title = title
        self.author = author
        self.date = date
        self.visibility = visibility
        self.friend_list = friend_list
        self.currenth = len(history)
        self.history = history
        self.text = history[(len(history)-1)]
        self.locked = locked

    def update(self, file_id, title, author, date, visibility, friend_list, history, locked):
        self.file_id = file_id
        self.title = title
        self.author = author
        self.date = date
        self.visibility = visibility
        self.friend_list = ast.literal_eval(friend_list)
        self.history = ast.literal_eval(history)
        self.currenth = len(self.history)
        self.text = history[(len(history)-1)]
        self.locked = locked

    #instance method
    def file_information(self):
        return '''
    File Information:
    ID: {}
    Name: {}
    Text : {}
    Author: {}
    Created On: {}
    Visibility: {}
    Shared With: {}
    Version: {}'''.format(self.file_id, self.title, self.text, self.author, self.date, self.visibility, self.friend_list, self.history)
    
    # move upward or downward in the file history
    def version_history(self, way):
        if way == 'forward':
            if self.currenth < len(self.history):
                self.currenth = self.currenth + 1
        else:
            if self.currenth > 0:
                self.currenth = self.currenth - 1

        self.text=self.history[self.currenth-1]
    # update text in file
    def text_update(self, new_text):
        self.text = new_text

    #push text in to the history   and save it to the csv  
    def save(self):
        self.history.append(self.text)
        self.currenth = self.currenth + 1
        self.save_file()

    # lock and unlock file
    def lock_unlock(self, lock):
        self.locked = not True

    # method to reads files from the database 
    def load(self,id):
        #assume the user is looking for file id 123
        with open('csvexample.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                if row['id'] == id:
                    print(row)
               
    # method to save file to the db
    def save_file(self):

        #creating a list with items to add to database
        myfile = [[self.file_id, self.title,self.author, self.date, self.visibility, self.friend_list, self.history,self.locked]]  
        
        #open the database
        database = open('csvexample.csv', 'a')  
        
        #write list to database
        with database:  
            writer = csv.writer(database)
            writer.writerows(myfile)
        
    def read_file(self):
        tmp = []
        #assume the user is looking for file id 123 and version 1
        print("I'm here")
        with open('csvexample.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                tmp.append([row['id'],row['title'],row['author'],row['visibility']])
        return tmp

#testing
#for file visibility : 0 = private, 1 = shared, 2 = public

# #create two files
# my_file = File(123, "My File", "This is the text in my file", "Julia", datetime.date.today(), 1, "Yannis", 1, False)
# my_file2 = File(213, "My Second File", "This is the text in my second file", "Julia", datetime.date.today(), 1, "Ronno", 1, False)
# #add both files to the db
# my_file.save_file()
# my_file2.save_file()
# #change the text in my_file
# #my_file.lock_unlock(False)
# #add file with new text and updated version to db
# #my_file.save_file()

# # method to reads files from the database 

# #look for a file in the db and print the file once found. The example is looking for file id = 123
# read_file()


# my_file = File(0, "idd", "guest", datetime.date.today(),'public',[''],['idsadasd','dsadsad'],False)
# my_file.save_file()
# my_file = File(1, "ok", "user", datetime.date.today(),'public',[''],['idsadasd','2134'],False)
# my_file.save_file()
#print([{'fileid':f,'title':t,'author':a,'visibility':v} for f,t,a,v in my_file.read_file() ])
