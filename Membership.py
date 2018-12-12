
Authority= 'admin'


class Membership:
    def __init__(self):
        self.SUL = ['2']
        self.OU = []
        self.APL = ['a','b']
        self.selected = ['1','2','3','b']

    def addsSelected(self,word):
        if word not in self.selected:
            self.selected.append(word)
        else:
            self.selected.remove(word)

    def remove(self):
        if Authority == 'admin':
            newSUL = [elem for elem in self.SUL if elem not in self.selected]
            newOU =[elem for elem in self.OU if elem not in self.selected]
            newAPL = [elem for elem in self.APL if elem not in self.selected]
        print(newSUL)
        print(newOU)
        print(newAPL)

    def accept(self):
        if Authority == 'admin':
            newOU = [elem for elem in self.APL if elem in self.selected] + [elem for elem in self.OU if elem not in self.selected]
            newAPL = [elem for elem in self.APL if elem not in self.selected]
            newSUL = [elem for elem in self.OU if elem in self.selected] + self.SUL

        print(newSUL)
        print(newOU)
        print(newAPL)

    def addOU(self):
        if Authority == 'admin':
            newOU = [elem for elem in self.APL if elem not in self.OU] + self.OU

        print(newOU)

    def update(self,newSUL,newOU,newAPL,newSelected):
        self.SUL.clear()
        self.OU.clear()
        self.APL.clear()
        self.selected.clear()

        self.SUL = newSUL
        self.OU = newOU
        self.APL = newAPL
        self.selected = newSelected






test = Membership()
test.addOU()


