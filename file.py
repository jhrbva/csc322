import datetime
import csv

class File:

    #class attribute
    file_visibility = ['private', 'shared', 'public']
    
    # initializer
    def __init__(self, file_id, title, text, author, date, visibility, friend_list, history, locked):
        self.file_id = file_id
        self.title = title
        self.text = text
        self.author = author
        self.date = date
        self.visibility = File.file_visibility[visibility]
        self.friend_list = friend_list
        self.history = history
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
            self.history = self.history + 1
        else:
            self.history = self.history - 1

    # update text in file
    def text_update(self, new_text):
        self.text = new_text
        self.history = self.history + 1

    # lock and unlock file
    def lock_unlock(self, lock):
        if lock == True:
            self.locked = True
            self.text_update("New text, New text, New text!")
        else:
            print("File is locked. Cannot make changes")

    # method to reads files from the database 
    def read_file(self):
        #assume the user is looking for file id 123
        id = '123'
        version = '2'
        with open('csvexample.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                if row['id'] == id and row['version'] == version :
                    print(row)
               
    # method to save file to the db
    def save_file(self):

        #creating a list with items to add to database
        myfile = [[self.file_id, self.title, self.text, self.author, self.date, self.visibility, self.friend_list, self.history]]  
        
        #open the database
        database = open('csvexample.csv', 'a')  
        
        #write list to database
        with database:  
            writer = csv.writer(database)
            writer.writerows(myfile)

    

#testing
#for file visibility : 0 = private, 1 = shared, 2 = public

#create two files
my_file = File(123, "My File", "This is the text in my file", "Julia", datetime.date.today(), 1, "Yannis", 1)
my_file2 = File(213, "My Second File", "This is the text in my second file", "Julia", datetime.date.today(), 1, "Ronno", 1)
#add both files to the db
my_file.save_file()
my_file2.save_file()
#look for a file in the db and print the file once found. The example is looking for file id = 123
my_file2.read_file()
#change the text in my_file
my_file.lock_unlock(False)
#add file with new text and updated version to db
my_file.save_file()