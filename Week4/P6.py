def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    '''player_option = None
    player_hand = None
    while player_option != 'e':
        player_option = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").lower()
        if player_option == 'n':
            player_hand = dealHand(HAND_SIZE)
            playHand(player_hand, wordList, HAND_SIZE)
            print()
        elif player_option == 'r':
            if player_hand != None:
                playHand(player_hand, wordList, HAND_SIZE)
                print()
            else:
                print("You've not played a hand yet. Please play a new hand first!\n")
        elif player_option != 'e':
            print("Invalid command.")'''
    play = True
    while play== True:
        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if game== 'e':
            break
            #return None
            break
        elif game == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            if game== 'e':
                break
        elif game== 'r':
            try:
                playHand(hand, wordList,HAND_SIZE)
            except:
                print('You have not played a hand yet. Please play a new hand first!')
                #game = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        else:
            print('Invalid command.')
            #game = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
