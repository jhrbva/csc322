from file import *
from user import *
import datetime


Authority = 'admin'


class File_Complaint(File):
    # class attribute
    complaint = "File Complaint"

    # initializer
    def __init__(self, complaint_date, complaint_id, file_id, complaint_author, complaint_text):
        self.complaint_date = complaint_date
        self.complaint_id = complaint_id
        self.file_id = file_id
        self.complaint_author = complaint_author
        self.complaint_text = complaint_text

    # instance method
    def complaint_information(self):
        return '''
    Complaint Information:
    Type: {}
    Date: {}
    ID: {}
    File: {}
    Author: {}
    Message: {}'''.format(self.complaint, self.complaint_date, self.complaint_id, self.file_id, self.complaint_author,
                          self.complaint_text)

    my_complaint = File_Complaint(datetime.date.today(), 321, 123, "Julia", "I don't like this file")
    print(my_complaint.complaint_information())

    print("the complaints have been sent to the owner")


class User_Complaint(User):
        # class attribute
    complaint = "User Complaint"

        # initializer
    def __init__(self, complaint_date, complaint_id, complainer_id, complainee_id, complaint_text):
        self.complaint_date = complaint_date
        self.complaint_id = complaint_id
        self.complainer_id = complainer_id
        self.complainee_id = complainee_id
        self.complaint_text = complaint_text

        # instance method
    def complaint_information(self):
        """ I display all the information about a complaint on a user """
        return '''
    Complaint Information:
    Type: {}
    Date: {}
    Complaint ID: {}
    Complainer: {}
    Complaint is About: {}
    Message: {}'''.format(self.complaint, self.complaint_date, self.complaint_id, self.complainer_id,
                          self.complainee_id, self.complaint_text)

    def remove(self):
        if Authority == 'admin':
           newIDL =[elem for elem in self.file_id if elem not in self.complaint_id]

        print(newIDL)



