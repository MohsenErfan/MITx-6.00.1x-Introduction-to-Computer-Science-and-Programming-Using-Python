"""Now you will implement the function hangman, which takes one parameter
- the secretWord the user is to guess. This starts up an interactive game
of Hangman between the user and the computer.
e sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part."""
from P3 import *
from P2 import *
from P1 import *
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print('Welcome to the game, Hangman!')
    len_word = len(secretWord)
    print('I am thinking of a word that is %d letters long.'%(len_word))
    print('-----------')
    n = 8
    lettersGuessed = ''
    gword = ''
    while n> 0 :
        print('You have %d guesses left.'% n)
        print('Available Letters: ',getAvailableLetters(lettersGuessed))
        letter = input('please guess a letter: ')
        #if letter in lettersGuessed:
        #    print('Oops! You\'ve already guessed that letter: %s'%gword)
        #    print('-----------')
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
            #letter = input('please guess a letter: ')
        if letter not in lettersGuessed:
            lettersGuessed += letter
            if letter in secretWord:
                gword = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess:%s'%gword)
                print('-----------')
                if gword == secretWord:
                    return 'Congratulations, you won!'
            else:
                n -= 1
                print('Oops! That letter is not in my word: _ ')
                print('-----------')

    else:
        print('Sorry, you ran out of guesses. The word was %s.'%secretWord)
hangman('bee')
