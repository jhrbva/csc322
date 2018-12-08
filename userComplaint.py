from user import *
import datetime

class User_Complaint(User):

    #class attribute
    complaint = "User Complaint"
    
    #initializer
    def __init__(self, complaint_date, complaint_id, complainer_id, complainee_id, complaint_text):
        self.complaint_date = complaint_date
        self.complaint_id = complaint_id
        self.complainer_id = complainer_id
        self.complainee_id = complainee_id
        self.complaint_text = complaint_text

    #instance method
    def complaint_information(self):
        """ I display all the information about a complaint on a user """
        return '''
    Complaint Information:
    Type: {}
    Date: {}
    Complaint ID: {}
    Complainer: {}
    Complaint is About: {}
    Message: {}'''.format(self.complaint, self.complaint_date, self.complaint_id, self.complainer_id, self.complainee_id, self.complaint_text)
        
#testing
my_complaint = User_Complaint(datetime.date.today(), "003", "008", "007", "007 is wack")
print(my_complaint.complaint_information())