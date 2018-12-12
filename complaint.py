Authority = 'admin'


class Complaint:
    def __init__(self):
        self.idl = ['2']
        self.complaintID = ['a', '1', '2']
        self.selected = ['1','2','a']

    def addsSelected(self,word):
        if word not in self.selected:
            self.selected.append(word)
        else:
            self.selected.remove(word)

    def accept(self):
        if Authority == 'admin':
            newComp = [elem for elem in self.selected if elem not in self.complaintID] + self.complaintID
            newidl =[elem for elem in self.idl if elem not in self.complaintID]

        print(newidl)
        print(newComp)

    def remove(self):
        if Authority == 'admin':
            newComp = [elem for elem in self.complaintID if elem not in self.selected]
            newidl = [elem for elem in self.idl if elem not in self.selected]

        print(newidl)
        print(newComp)

    def update(self, newidl, newComp, newSelected):

        self.idl.clear()
        self.complaintID.clear()
        self.selected.clear()

        self.idl = newidl
        self.complaintID = newComp
        self.selected = newSelected

test = Complaint()
test.remove()