import random

class RandomWord(object):
    """
    read the words from an outside file and return one of those words, randomly chosen
    """
    def __init__(self, filename):
        with open(filename) as f:
            words_list = []
            for line in f:
                words_list.append(line.rstrip('\r\n'))
            self.word = random.choice(words_list)
            print(words_list)
            print(self.word)

    def display(self, guessed_letters_list):
        """
        Function to display the secret word with the letters that have been correctly guessed.
        """
        word_to_display = ""
        for letter in self.word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "
            else:
                word_to_display += " _ "
        print ("This is your word so far:", word_to_display, "\n")
        return word_to_display



    #             if letter_guess not in self.secret_word.word:
    #                 print (random.choice(self.WRONG_ANSWER_PUTDOWNS))
    #                 self.num_incorrect_guesses_made += 1
    #                 self.jumperman.draw(self.num_incorrect_guesses_made)
    #             else:
    #                 print ("You chose wisely!\n")
    #                 self.jumperman.draw(self.num_incorrect_guesses_made)
        
