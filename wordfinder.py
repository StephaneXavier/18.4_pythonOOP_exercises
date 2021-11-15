
from random import randint

class WordFinder:
    """
    Will generate an array of words from a text file.

    """
    def __init__(self,path):
        # the file only needs to be open once to be used in making self.words_list
        # We don't care about saving it as a value in the new instance 
        open_file = open(path)
        # use the open_file as arg for self.word_list_generator (has to be self. as it is a method present in 
        # new instance of WordFinder) to create self.words_list
        self.words_list = self.word_list_generator(open_file) 
        print(f'{len(self.words_list)} words read')
        # open_file is now "forgotten" at every new instance of WordFinder

    
    def word_list_generator(self, param):
        return [line.strip() for line in param ]

    def random(self):
        index = randint(0,len(self.words_list))
        return self.words_list[index]

    

class SpecialWordFinder(WordFinder):

    def word_list(self, open_file):
        return [line.strip() for line in open_file if line.strip() and not line.startswith('#')]
  