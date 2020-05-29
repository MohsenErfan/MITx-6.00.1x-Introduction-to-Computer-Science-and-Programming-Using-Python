def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    new_hand = hand.copy()
    for letter in word:
        if letter in hand:
            new_hand[letter] -= 1
            if new_hand[letter] < 0:
                return False
        else:
            return False
    if word not in wordList:
        return False
    return True
