from game.jumperman import Jumperman
from game.ramdomword import RandomWord
from game.guessed_letters import Guessed_letters
from game.word_list import word_list


class Game(object):
    
     
    def __init__(self):
        filename = "game\word_list.txt"
        self.secret_word = RandomWord(filename)
        self.jumperman = Jumperman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
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
        print(self.guessed_letters)


       
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        #check in ramdom words or new class to do the calculation

        #if letter is in the ramdom word continue otherwise delete it and delete one life from the Jumper pics

        
        while self.num_incorrect_guesses_made < 5:
            if len(self.guessed_letters) == 0:
                self.secret_word.display(self.guessed_letters)
            letter_guess = input("Please guess a letter: ").lower()
 
            if letter_guess not in self.guessed_letters:
                self.guessed_letters.append(letter_guess)

                if letter_guess not in self.secret_word.word:
                   
                    self.num_incorrect_guesses_made += 1
                    self.jumperman.draw(self.num_incorrect_guesses_made)
                else:
                    print ("You chose wisely!\n")
                    self.jumperman.draw(self.num_incorrect_guesses_made)
            else:
                print ("You've already guessed the letter '%s', please choose a new letter." % letter_guess)

            current_word = self.secret_word.display(self.guessed_letters)
            print ("These are the letters you've already guessed: ", self.guessed_letters)
            if "_" not in current_word:
                print ("Congratulations! You've won!")
       
   
        
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
 
 

 
