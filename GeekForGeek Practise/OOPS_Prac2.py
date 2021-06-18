'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Python program to build flashcard using class in Python.'''

class flashcard:
    def __init__(self, word, meaning):
        self.Word = word
        self.Meaning = meaning

    def flash(self):
        print(f'{word}: {meaning}')

if __name__ == '__main__':

    word = input()
    meaning = input()
    flash = flashcard(word, meaning)
    flash.flash()