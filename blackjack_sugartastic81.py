# sugartastic81 Black Jack in Python

# import the classes
import random, time, os

# set a dictionary for the the cards of a deck
card_values = {2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Ace', 12: 'Jack', 13: 'Queen', 14: 'King'}
card_colors = {'h': 'hearts', 'd': 'diamonds', 'c': 'clubs', 's': 'spades'}

# define a class for the play cards
class class_card:
    # init method
    def __init__(self, value, color):
        self.value = value
        self.color = color
    # string method
    def __str__(self):
        return (card_values[self.value] + " of " + card_colors[self.color])

# function which counts the value of a hand and returns it
def counthand(hand):
    handsum=0
    for card in hand:
        if card.value > 11:
            handsum += 10
        elif card.value == 11: # Ace is 11 or 1, but it is ignored and always counts 11 in this game
            handsum += 11
        else:
            handsum += card.value
    return(handsum)

# function which prints the hand of the dealer, but shows only the first one and hides the other one
def printhandofdealer(hand):
    print("Hand of dealer: ", end ="")
    numofcards = len(hand)
    i = 1
    for card in hand:
        if(i == 1):
            print(card, end =", ")
        else:
            print("***hidden***")
        i += 1

# fucntion which prints the hand of the player
def printhandof(hand, whichone):
    print("Hand of "+whichone+": ", end ="")
    numofcards = len(hand)
    i = 1
    for card in hand:
        if(i < numofcards):
            print(card, end =", ")
        else:
            print(card)
        i += 1


print("\n*** LETS PLAY A ROUND OF BLACK JACK IN THE PYTHON CASINO ***")
playAgain = True

# This loop executes until the player inputs (E)xit
while playAgain:
    print("\nDealer shuffles a deck of cards for playing black jack!")

    # Initialize a deck of cards
    card_deck = []
    for i in card_values:
        for j in card_colors:
            card_deck.append(class_card(i,j))

    # Shuffles the deck 5 times
    for x in range(0,4):
        random.shuffle(card_deck)

    # Initialize a hands for the dealer and for the player
    hand = {'player':[],'dealer':[]}
    # Initialize the scores for the dealer and for the player
    handscore = {'player': 0, 'dealer': 0 }

    # Assign the dealer and the player their first two cards
    hand['player'].append(card_deck.pop(0)) # takes top card on the stack into the players hand
    hand['dealer'].append(card_deck.pop(0)) # takes top card on the stack into the dealer hand
    handscore['dealer'] = counthand(hand['dealer']) # only counts open card for player
    hand['player'].append(card_deck.pop(0)) # takes top card on the stack into the players hand
    hand['dealer'].append(card_deck.pop(0)) # takes top card on the stack into the dealer hand
    handscore['player'] = counthand(hand['player'])

    playHuman = True
    lostHuman = False
    exitGame = False

    # This loop is executed as long as the player takes actions
    while playHuman:
        os.system('clear')
        # Show the player his two cards and the dealers first card the other remains hidden
        print()
        printhandof(hand['player'], "player")
        printhandofdealer(hand['dealer'])
        print("Score: Player " + str(handscore['player']) + ", Dealer " + str(handscore['dealer'])+"")

        # If player already has a blackjack, round is over and no input is needed
        if handscore['player'] != 21: # if he has no blackjack
            userInput = ''
            inputCycle = True
            # Loop executes until player inputes an asked action
            while inputCycle:
                userInput = input("Please enter the desired action. Type (H)it, (S)tand or (E)xit: ").upper()
                # There are many forms of the asked input possible
                if (len(userInput) == 1 and userInput[:1] in ['H','S','E']) or userInput in ["(H)","(S)","(E)","HIT","STAND","EXIT","(H)IT","(S)TAND","(E)XIT"]:
                    inputCycle = False
                else:
                    print("Invalid input. Please type in a possible action.")

            # if player chooses to hit, he gets another card
            if userInput[:1] == 'H' or userInput[:3] == "(H)":
                print("\nPlayer choose to hit a card.")
                hand['player'].append(card_deck.pop(0)) # takes top card on the stack into the players hand
                handscore['player'] = counthand(hand['player'])
                if handscore['player'] >= 21:
                    playHuman = False # if player has 21 or more points he will not get another card
                    if handscore['player'] > 21: # if player has over 21 points, he is overbought and lost
                        lostHuman = True
            # if player chose to stand, dealer is on turn
            elif userInput[:1] == 'S' or userInput[:3] == "(S)": # if player wants to stay
                playHuman = False
            else: # this will exit the game.
                exitGame = True
                playHuman = False
                playAgain = False
        else:
            playHuman = False
            print("\nPlayer has a served black jack.")
    if not exitGame:
        print()
        if not playHuman and not lostHuman and handscore['player'] != 21:
            print("Player choose to stay.\n")
        # now the dealers hidden card is counted and shown
        handscore['dealer'] = counthand(hand['dealer'])
        printhandof(hand['player'], "player")
        printhandof(hand['dealer'], "dealer")
        print("Score: Player " + str(handscore['player']) + ", Dealer " + str(handscore['dealer']))

        if handscore['player'] != 21:  # if he has no blackjack
            # if player hasn't lost because score over 21 and plyer no black jack
            if not lostHuman and handscore['player'] != 21:
                if handscore['dealer'] < 17: # if dealers hand is under 17, he has to take another card
                    playDealer = True
                else: # with 17 and more he has to stay
                    playDealer = False
                while playDealer: # dealer gets another card
                    print("\nDealer has "+ str(handscore['dealer'])+" and hits a card.\n")
                    time.sleep(1) # short waiting time for the dealer -> more realism
                    hand['dealer'].append(card_deck.pop(0)) # takes top card on the stack into the dealers hand
                    handscore['dealer'] = counthand(hand['dealer'])
                    printhandof(hand['player'], "player")
                    printhandof(hand['dealer'], "dealer")
                    print("Score: Player " + str(handscore['player']) + ", Dealer " + str(handscore['dealer']))
                    if handscore['dealer'] >= 17: # with score 17 and up dealer gets no more cards
                        playDealer = False
# End of the round
        print()
        if lostHuman:
            print("*** DEALER wins with score "+str(handscore['dealer']) + ". Player has score " + str(handscore['player'])+ ". ***")
        else:
            if handscore['player'] == 21:
                print("*** PLAYER wins with score "+str(handscore['player']) + " (BLACK JACK). Dealer has score " + str(handscore['dealer'])+ ". ***")
            else:
                if handscore['dealer'] > 21:
                    print("*** PLAYER wins with score "+str(handscore['player']) + ". Dealer has score " + str(handscore['dealer'])+ ". ***")
                else:
                    if handscore['dealer'] == 21:
                        print("*** DEALER wins with score "+str(handscore['dealer']) + " (BLACK JACK). Player has score " + str(handscore['player'])+ ". ***")
                    else:
                        if handscore['dealer'] > handscore['player']:
                            print("*** DEALER wins with score "+str(handscore['dealer']) + ". Player has score " + str(handscore['player'])+ ". ***")
                        elif handscore['dealer'] < handscore['player']:
                            print("*** PLAYER wins with score "+str(handscore['player']) + ". Dealer has score " + str(handscore['dealer'])+ ". ***")
                        elif handscore['dealer'] == handscore['player']:
                            print("*** TIE. Player has score "+str(handscore['player']) + " and dealer has " + str(handscore['dealer'])+ ". ***")
                        else:
                            print("*** PROBLEM. Calculation fault.")

# Question if a new round should be played.
        inputCycle = True
        userInput = ''
        time.sleep(3) # short waiting time for more realism

        while inputCycle:
            userInput = input("\nRound is over. Please enter the desired action. Type (P)lay again or (E)xit: ").upper()
            if (len(userInput) == 1 and userInput[:1] in ['P','E']) or userInput in ["(P)","(E)","PLAY","EXIT","(P)LAY","(P)LAY AGAIN","PLAY AGAIN","(E)XIT"]:
                inputCycle = False
            else:
                print("Invalid input. Please type in a possible action.")
        if userInput[:1] == 'P' or userInput[:3] == "(P)":
            playAgain = True
        else: # this will exit the game.
            exitGame = True
            playHuman = False
            playAgain = False

print("\n\n*** GOODBYE. HOPE TO SEE YOU SOON AGAIN IN PYTHON CASINO ***\n")

