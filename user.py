import csv

class User:

    #class attribute
    user_type = ["ordinary", "super"]
    
    # initializer
    def __init__(self, user_id,  user_type, username, password, files_visited):
        self.user_id = user_id
        self.user_type = user_type
        self.username = username
        self.password = password
        self.files_visited = files_visited
    def update(self, user_id,  user_type, username, password, files_visited):
        self.user_id = user_id
        self.user_type = user_type
        self.username = username
        self.password = password
        self.files_visited = files_visited
        
    #instance method
    def user_information(self):
        """I print out user information, except password"""
        
        return '''
    User Information:
    ID: {}
    User Type: {}
    Name: {}
    Files Visited: {}'''.format(self.user_id, self.user_type, self.username, self.files_visited)

     # method to user info to the db
    def save_user(self):
        #creating a list with items to add to database
        user = [[self.user_id, self.user_type, self.username,self.password, self.files_visited]]  
        
        #open the database
        database = open('userdatabase.csv', 'a')  
        
        #write list to database
        with database:  
            writer = csv.writer(database)
            writer.writerows(user)

    # method to reads user information from the database 
    def find_user(self):
        #assume that you are looking for user ID = 188
        id = '188'
        with open('userdatabase.csv', newline='') as myFile:  
            reader = csv.DictReader(myFile)
            for row in reader:
                if row['id'] == id :
                    print(row)

#testing
# my_user = User(999,'guest','guest','guest',[""])
# my_user.save_user()
# my_user = User(0,'admin','admin','admin',[""])
# my_user.save_user()
# my_user = User(1,'super','super','super',[""])
# my_user.save_user()
# my_user = User(2,'ordinay','o','o',[""])
# my_user.save_user()