from game.jumperman import Jumperman
from game.ramdomword import RandomWord



class Game(object):

    
    def __init__(self):
        
        self.random = RandomWord().getter()
        self.secret_word = RandomWord()
        self.jumperman = Jumperman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = [ ]
        self._is_playing = True
        self.letter_guess = ""

    def play(self):
        """
        The main function that begins a new game of Jumperman.
        """

        print ("\n****** Welcome to Jumperman! ******\n")
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
             
    


    def _get_inputs(self):
        """Gets the guess letter.
        
        Args:
            self (Director): An instance of Director.
        """

        print()
 
        self.letter_guess = input("Guess a letter: ")

        self.guessed_letters.append(self.letter_guess)
        

         
       
        
    def _do_updates(self):
            """Keeps watch on where the guess letter is on the secret word.

            Args:
                self (Director): An instance of Director.
            """
         
            if self.letter_guess not in self.random:
                   
                    self.num_incorrect_guesses_made += 1
                    self.jumperman.draw(self.num_incorrect_guesses_made)

                    if self.num_incorrect_guesses_made == 5:
                        self._is_playing = False
            else:
                    print ("You chose wisely!\n")
                    self.jumperman.draw(self.num_incorrect_guesses_made)
         
            #
            current_word = self.secret_word.display(self.guessed_letters)
            print ("These are the letters you've already choosen so far: ", self.guessed_letters)
            if "_" not in current_word:
                print ("Congratulations! You've won!")
                self._is_playing = False
  