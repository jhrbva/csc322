Authority = 'admin'


class Complaint:
    def __init__(self):
        self.idl = ['2']
        self.complaintID = ['a', '1', '2']

    def remove(self):
        if Authority == 'admin':
           newidl =[elem for elem in self.idl if elem not in self.complaintID]

        print(newidl)


test = Complaint()
test.remove()

