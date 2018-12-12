
Authority= 'admin'


class TabooList:
    def __init__(self):
        self.SuggL = ['1', '2', '3']
        self.Taboo = ['f', 'd', 'z']
        self.selected = ['3', 'a', '2']

    def addsSelected(self,word):
        if word not in self.selected:
            self.selected.append(word)
        else:
            self.selected.remove(word)

    def remove(self):
        if Authority == 'admin':
            newSugL = [elem for elem in self.SuggL if elem not in self.selected]
            newTaboo = [elem for elem in self.Taboo if elem not in self.selected]

        print(newSugL)
        print(newTaboo)

    def accept(self):
        if Authority == 'admin':
            newSugL = [elem for elem in self.selected if elem not in self.SuggL] + self.SuggL
            newTaboo = [elem for elem in self.SuggL if elem not in self.Taboo] + self.Taboo

        print(newSugL)
        print(newTaboo)



    def update(self,newSugL,newTaboo,newSelected):
        self.SuggL.clear()
        self.Taboo.clear()
        self.selected.clear()

        self.SuggL = newSugL
        self.Taboo = newTaboo
        self.selected= newSelected


test = TabooList()
test.accept()


