from collections import OrderedDict

class Taboo_List():

    # initializer (tabooList_file = "tabooList.txt", system_file = any file in the system, will use "testFile.txt" for this)
    def __init__(self, tabooList_file, taboo_word, system_file):
        self.tabooList_file = tabooList_file
        self.taboo_word = taboo_word
        self.system_file = system_file

    # adding a taboo word to the list method
    def add_word(self):
        """ I add words to the Taboo List """
        word = raw_input('Enter the taboo word: ')
        with open(self.tabooList_file, 'r') as file:
            filedata = file.read()
            # THIS CONDITIONAL IS NOT WORKING - IT JUST ADD REPEATED WORDS TO THE FILE
            if filedata == word :
                print('This word is already on the list')
            else :
                with open(self.tabooList_file, 'a') as file:
                    file.write(word + '\n')
        print("Your word has been added to the list")

    
    # deleting word from taboo list method
    def remove_word(self):
        """ I remove words to the Taboo List """
        #word = raw_input("Enter the taboo word: ")
        # Read in the file
        with open(self.tabooList_file, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(self.taboo_word, ' ')

        # Write the file out again
        with open(self.tabooList_file, 'w') as file:
            file.write(filedata)
        print("The word has been removed")
        
    #decision making
    def add_or_delete(self):
        """ I help decide if the user will add or delete a taboo word from the list """
        user_action = raw_input("Type A to add the word to the list, type R to remove the word from the list: ")

        if user_action == "A":
            self.add_word()
        if user_action == "R":
            self.remove_word()

    # taboo word text scanner
    def text_scanner(self):
        """ I help scan strings to find taboo words and delete them from text """
        file_text = self.system_file.lower().split()
        bad_words = self.tabooList_file.split()

        clean_file = list(set(file_text).difference(set(bad_words)))
        print(clean_file)

        return clean_file

#testing
tabooWord = Taboo_List("jackass shit asswhole bastard", "idiot", "hello you bastard nice to meet you jackass").text_scanner()
#tabooWord = Taboo_List("tabooList.txt", "idiot", "testFile.txt").add_or_delete()

