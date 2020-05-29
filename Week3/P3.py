"""Next, implement the function getAvailableLetters that takes in one parameter
 - a list of letters, lettersGuessed. This function returns a string that is
 comprised of lowercase English letters - all lowercase English letters that are
 not in lettersGuessed."""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    all = string.ascii_lowercase
    not_in = ''
    for l in all:
        if l not in lettersGuessed:
            not_in += l
    return not_in
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
