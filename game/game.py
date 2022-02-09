from game.jumperman import Jumperman
from game.ramdomword import RandomWord



class Game(object):

    
    def __init__(self):
        filename = "game\word_list.txt"
        self.secret_word = RandomWord(filename)
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
            self._do_outputs()
    


    def _get_inputs(self):
        """Moves the seeker to a new location.
        
        Args:
            self (Director): An instance of Director.
        """

        print()


        self.letter_guess = input("Guess a letter: ")

        self.guessed_letters.append(self.letter_guess)
        print(self.guessed_letters)


       
        
    def _do_updates(self):
            """Keeps watch on where the seeker is moving.

            Args:
                self (Director): An instance of Director.
            """
            #check in ramdom words or new class to do the calculation

            #if letter is in the ramdom word continue otherwise delete it and delete one life from the Jumper pics

        
     



            # if len(self.guessed_letters) == 0:               

            #     self.secret_word.display(self.guessed_letters)
            # letter_guess = input("Please guess a letter: ").lower()
            


            # if letter_guess not in self.guessed_letters:
            #     self.guessed_letters.append(letter_guess)

            
         
             

            if self.letter_guess not in self.secret_word.word:
                   
                    self.num_incorrect_guesses_made += 1
                    self.jumperman.draw(self.num_incorrect_guesses_made)

                    if self.num_incorrect_guesses_made == 5:
                        self._is_playing = False
            else:
                    print ("You chose wisely!\n")
                    self.jumperman.draw(self.num_incorrect_guesses_made)
         
            print ("You've already guessed the letter '%s', please choose a new letter." % self.guessed_letters)

            current_word = self.secret_word.display(self.guessed_letters)
            print ("These are the letters you've already choosen so far: ", self.guessed_letters)
            if "_" not in current_word:
                print ("Congratulations! You've won!")
       
   
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.


        """
        if not self._is_playing:
            return
         
        
      
 

 
