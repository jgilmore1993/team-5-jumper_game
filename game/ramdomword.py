import random
import re

class RandomWord(object):
    """
    read the words from an outside file and return one of those words, randomly chosen
    """
    def __init__(self):
        
            word_list = ["anarchism", "capitalism", "communism", "socialism"]
            self._word = random.choice(word_list)
            
            
            

    def display(self, guessed_letters_list):
        """
        Function to display the secret word with the letters that have been correctly guessed.
        """
        word_to_display = ""
        for letter in self._word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "
            else:
                word_to_display += " _ "
        print ("This is your word so far:", word_to_display, "\n")
        return word_to_display
    def getter(self):

        

       return self._word 


        
