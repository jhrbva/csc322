class Membership:
    def __init__(self,SUL,OU,APL,Authority):
        self.SUL = SUL
        self.OU = OU
        self.APL = APL
        self.selected = []
        self.Authority = Authority

    def addsSelected(self,word):
        if word not in self.selected:
            self.selected.append(word)
        else:
            self.selected.remove(word)

    def remove(self):
        if self.Authority == 'admin':
            newSUL = [elem for elem in self.SUL if elem not in self.selected]
        else:
            newSUL = self.SUL
        newOU =[elem for elem in self.OU if elem not in self.selected]
        newAPL = [elem for elem in self.APL if elem not in self.selected]
        self.update(newSUL,newOU,newAPL,[])
        print(newSUL)
        print(newOU)
        print(newAPL)

    def accept(self):
        if self.Authority == 'admin':
            newSUL = [elem for elem in self.OU if elem in self.selected] + self.SUL
        else:
            newSUL = self.SUL
        newOU = [elem for elem in self.APL if elem in self.selected] + [elem for elem in self.OU if elem not in self.selected]
        newAPL = [elem for elem in self.APL if elem not in self.selected]

        self.update(newSUL,newOU,newAPL,[])
        print(newSUL)
        print(newOU)
        print(newAPL)

    def addOU(self,ou):
        k = []
        k.append(ou)
        print(k)
        if ou not in self.SUL:
            newOU = [elem for elem in self.APL if elem in k] + [elem for elem in self.OU if elem not in k]
            newAPL = [elem for elem in self.APL if elem not in k]
            self.update(self.SUL,newOU,newAPL,self.selected)
            print(newOU)
            print(newAPL)

    def update(self,newSUL,newOU,newAPL,newSelected):
        self.SUL.clear()
        self.OU.clear()
        self.APL.clear()
        self.selected.clear()
        self.SUL = newSUL
        self.OU = newOU
        self.APL = newAPL
        self.selected = newSelected





