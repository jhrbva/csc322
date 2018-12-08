class User:

    #class attribute
    user_type = ["ordinary", "super"]
    
    # initializer
    def __init__(self, user_id,  user_type, username, password, files_visited):
        self.user_id = user_id
        self.user_type = User.user_type[user_type]
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


#testing
my_profile = User(1, 0, "juliaa", "password", "123, 234")
print(my_profile.user_information())
    
#   question:
#   for some reason if I make the user ID greater than a single integer, the code doesn't work.
#   should we make the user ID a string? should we make all IDs strings?
