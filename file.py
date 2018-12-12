import datetime
import csv

class File:

    #class attribute
    file_visibility = ['private', 'shared', 'public']
    
    # initializer
    def __init__(self, file_id, title, text, author, date, visibility, friend_list, history):
        self.file_id = file_id
        self.title = title
        self.text = text
        self.author = author
        self.date = date
        self.visibility = File.file_visibility[visibility]
        self.friend_list = friend_list
        self.history = history

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

    # method to reads files from the database 
    def read_file(self):
        #assume the user is looking for file id 123
        id = '123'
        with open('csvexample.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                if row['id'] == id :
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

    def search_file(self) :
        with open('csvexample.csv', newline='') as myFile:  
            reader = csv.reader(myFile)
            for row in reader:
                print(row)


#testing
#for file visibility : 0 = private, 1 = shared, 2 = public

my_file = File(123, "My File", "This is the text in my file", "Julia", datetime.date.today(), 1, "Yannis", 1)
#print('First version of file:')
#print(my_file.file_information())
#my_file.text_update('My file is so much better now that I updated the text')
#print('Modified version of file:')
#print(my_file.file_information())
my_file.read_file()
#my_file.save_file()
