from game.jumperman import Jumperman
from game.ramdomword import RandomWord


class Game(object):
    
     
    def __init__(self):
        filename = "game\word_list.txt"
        self.secret_word = RandomWord(filename)
        self.jumperman = Jumperman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = []
        self._is_playing = True

    def play(self):
        """
        The main function that begins a new game of Jumperman.
        """

        print ("\n****** Welcome to Jumperman! ******\n")
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()



    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        print( self.jumperman)
        print()
        
       
        guess_letter = input("Guess a letter: ")

        self.guessed_letters.append(guess_letter)


       
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        #check in ramdom words or new class to do the calculation

        #if letter is in the ramdom word continue otherwise delete it and delete one life from the Jumper pics
   
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        # print the current pic from jumperman class and the guessed letter so far. 
        # 
        # 
        # 
        #   
        #Enos sugestion code. 
        # hint = self._hider.get_hint()
        # self._terminal_service.write_text(hint)
        # if self._hider.is_found():
        #     self._is_playing = False

        # option = raw_input("Do you need the rules explained to you? Y/n: ")

    #    # if option.lower() == "y": 
    #         print ("\n Instructions: \n")
    #         print ("A word will be chosen at random from the dictionary. Each turn you guess a letter.\n")
    #         print("Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n")
    #         print("When your hangman looks like this: O-|-< ...you're dead!\n")
    #     print ("Let's play Jumperman!\n")

    #     # Initialize the number of incorrect guesses made to 0
    #     while self.num_incorrect_guesses_made < 5:
    #         if len(self.guessed_letters) == 0:
    #             self.secret_word.display(self.guessed_letters)
    #         letter_guess = raw_input("Please guess a letter: ").lower()

    #         # Don't let them guess a non-alpha letter.
    #         while letter_guess.isalpha() is False:
    #             letter_guess = raw_input.lower()("No special characters allowed! Only enter a letter, please: ")
    #         # Once a valid letter is chosen, add it to guessed_letters
    #         if letter_guess not in self.guessed_letters:
    #             self.guessed_letters.append(letter_guess)

    #             if letter_guess not in self.secret_word.word:
    #                 print (random.choice(self.WRONG_ANSWER_PUTDOWNS))
    #                 self.num_incorrect_guesses_made += 1
    #                 self.jumperman.draw(self.num_incorrect_guesses_made)
    #             else:
    #                 print ("You chose wisely!\n")
    #                 self.jumperman.draw(self.num_incorrect_guesses_made)
    #         else:
    #             print ("You've already guessed the letter '%s', please choose a new letter." % letter_guess)

    #         current_word = self.secret_word.display(self.guessed_letters)
    #         print ("These are the letters you've already guessed: ", self.guessed_letters)
    #         if "_" not in current_word:
    #             print ("Congratulations! You've won!")
    #             # sys.exit()