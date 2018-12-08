from file import *

class File_Complaint(File):

    #class attribute
    complaint = "File Complaint"
    
    #initializer
    def __init__(self, complaint_date, complaint_id, file_id, complaint_author, complaint_text):
        self.complaint_date = complaint_date
        self.complaint_id = complaint_id
        self.file_id = file_id
        self.complaint_author = complaint_author
        self.complaint_text = complaint_text

    #instance method
    def complaint_information(self):
        return '''
    Complaint Information:
    Type: {}
    Date: {}
    ID: {}
    File: {}
    Author: {}
    Message: {}'''.format(self.complaint, self.complaint_date, self.complaint_id, self.file_id, self.complaint_author, self.complaint_text)


#testing
my_complaint = File_Complaint(datetime.date.today(), 321, 123, "Julia", "I don't like this file")
print(my_complaint.complaint_information())

    
# I'm creating two different complaint classes because I think it will be easier to make them children of another class
# One complaint class is a user complaint so is a child of user and the other is a file complaint so child of file class
