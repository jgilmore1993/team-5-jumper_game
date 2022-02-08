class Jumperman(object):

    JUMPERMAN_PICS = [''' 
        --------
        _______
       /       \ 
       \ ______/
        \     /
         \   /
           O
          /|\ 
          / \  
    ^^^^^^^^^^^^^^^^^^
    ''' , ''' 
       ----------
       /       \ 
       \ ______/
        \     /
         \   /
           O
          /|\ 
          / \ 
    ^^^^^^^^^^^^^^^^^^ 
    ''', ''' 
       ---------- 
        \     /
         \   /
           O
          /|\ 
          / \ 
    ^^^^^^^^^^^^^^^^^^ 
    
    ''',''' 
      ---------- 
        
         \   /
           O
          /|\ 
          / \ 
    ^^^^^^^^^^^^^^^^^^ 
    ''' , '''
      ---------- 
        
        
           O
          /|\ 
          / \ 
    ^^^^^^^^^^^^^^^^^^
    
     ''', '''
       ---------- 
        
        
           x
          /|\ 
          / \ 
    ^^^^^^^^^^^^^^^^^^
    ''']
    def __init__(self):
        self._jumperman = self.JUMPERMAN_PICS[0]

    def draw(self, num_incorrect_guesses_made):
        """
        Function to display the updated status of the jumperman based on the number of incorrect guesses the player has made.
        """
        self._jumperman = self.JUMPERMAN_PICS[num_incorrect_guesses_made]

        print(self.JUMPERMAN_PICS[num_incorrect_guesses_made] )
        

        # if num_incorrect_guesses_made == 5:
        #     print ("You died!!")
