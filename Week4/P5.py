def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    score2 = 0
    number = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand

        print('Current Hand:',end=" ")
        (displayHand(hand))
        number +=1
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')
        #print(word)
        # If the input is a single period:
        if word == '.':
            break
            # End the game (break out of the loop)
        else:
            if isValidWord(word, hand, wordList)==False:
                print('Invalid word, please try again ')
                print()
        # Otherwise (the input is not a single period):

            # If the word is not valid:

                # Reject invalid word (print a message followed by a blank line)
            elif isValidWord(word, hand, wordList):
            # Otherwise (the word is valid):
                score = getWordScore(word, n)
                score2 += score
                print("{0} earned {1} points. Total: {2} points ".format(word, score, score2 ))
                print()
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                #print('Current Hand:', end=" ")
                #displayHand(hand)
                # Update the hand
    if word == '.':
        print('Goodbye! Total score: {0} points '.format(score2))
    elif calculateHandlen(hand) == 0:
        print('Run out of letters. Total score: {0} '.format(score2))
