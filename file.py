import datetime

class File:

    # initializer
    def __init__(self, file_id, title, author, date, authority, friend_list, history):
        self.file_id = file_id
        self.title = title
        self.author = author
        self.date = date
        self.authority = authority
        self.friend_list = friend_list
        self.history = history

    #instance method
    def file_information(self):
        return '''
    File Information:
    ID: {}
    Name: {}
    Author: {}
    Created On: {}
    Visibility: {}
    Shared With: {}
    Version: {}'''.format(self.file_id, self.title, self.author, self.date, self.authority, self.friend_list, self.history)


#testing
my_file = File(123, "My File", "Julia", datetime.date.today(), "private", "Yannis", "0.1")
print(my_file.file_information())
    
#   question:
#   how can we prevent date from changing everytime we change something on the file? or do we want the date to change?
