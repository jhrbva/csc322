import fileinput

class Taboo_List():

    #initializer
    def __init__(self, file_name, word):
        self.file_name = file_name
        self.word = word

    # write method
    def add_word(self):
        """ I add words to the Taboo List """
        word = input("Enter the taboo word: ")
        with open(self.file_name, "a+") as f:
            f.write(word + '\n')

        print("Your word has been added to the list")

    #delete method
    def remove_word(self):
        """ I remove words to the Taboo List """
        word = input("Enter the taboo word: ")
        # Read in the file
        with open(self.file_name, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(word, ' ')

        # Write the file out again
        with open(self.file_name, 'w') as file:
            file.write(filedata)

        print("The word has been removed")
        
    #decision making
    def add_or_delete(self):
        """ I help decide if the user will add or delete a taboo word from the list """
        user_action = input("Type A to add the word to the list, type R to remove the word from the list: ")

        if user_action == "A":
            self.add_word()
        if user_action == "R":
            self.remove_word()
       
#testing
tabooWord = Taboo_List("tabooList.txt", "")

