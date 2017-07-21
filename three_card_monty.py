# issue: can't tell if left happens twice
# invisible moves happen occasionally?
# player given double-or-nothing option
# docstrings
# tests

import os
import time
import random


def clear_screen():
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(seconds):
    """Pause for the number of seconds specified as argument."""
    time.sleep(seconds)

def print_player_money(player_money):
    """Display the amount of dollars the player currently has."""
    print(f"""

===========================
|| You have {player_money} dollars. ||
===========================

    """)

def ascii_cards(card_display_list):
    """Prints to screen three ascii art cards, face up."""
    clear_screen()
    print("""
   ___    ___    ___
  |{}  |  |{}  |  |{}  |
  |   |  |   |  |   |
  |  {}|  |  {}|  |  {}|
   ---    ---    ---
    """.format(card_display_list[0], card_display_list[1], card_display_list[2], card_display_list[0], card_display_list[1], card_display_list[2]))

def ascii_cards_backs():
    """Prints to screen three ascii art cards, face down.

    >>>ascii_cards_backs()
   ___    ___    ___
  |///|  |///|  |///|
  |///|  |///|  |///|
  |///|  |///|  |///|
   ---    ---    ---



    """
    clear_screen()
    print("""
   ___    ___    ___
  |///|  |///|  |///|
  |///|  |///|  |///|
  |///|  |///|  |///|
   ---    ---    ---
    """)

def card_shuffle(correct_card):
    """Approximates the shuffling of the three cards
     by printing to screen the movements of the Ace card
     with a slight pause between each move."""
    for _ in range(10):
        ascii_cards_backs()
        print("\n\n\t")
        if correct_card == 0:
            card_move_decider = random.randint(0,1)
            if card_move_decider == 0:
                print("Stay")
            else:
                print("Right")
                correct_card = 1
            pause(1)
        elif correct_card == 1:
            card_move_decider = random.randint(0,2)
            if card_move_decider == 0:
                print("Left")
                correct_card = 0
            elif card_move_decider == 1:
                print("Stay")
            else:
                print("Right")
                correct_card = 2
            pause(1)
        else:
            card_move_decider = random.randint(0,1)
            if card_move_decider == 0:
                print("Left")
                correct_card = 1
            else:
                print("Stay")
            pause(1)
    return correct_card

def win_round(amount, correct_card):
    """Player has won the round. Shows the cards face up, adds dollars to player money and displays congratulatory message.""""
    clear_screen()
    card_display_list = [' ', ' ', ' ']
    card_display_list[correct_card] = 'A'
    ascii_cards(card_display_list)
    global player_money
    player_money += int(amount)
    print(f'"OK, well done. You picked the Ace."\n\nYou won {amount} dollars!')
    pause(3)
    # random congratulatory message from several


def lose_round(amount, correct_card):
    """Player has lost the round. Shows the cards face up, subtracts dollars from player money and displays conciliatory message.""""
    clear_screen()
    card_display_list = [' ', ' ', ' ']
    card_display_list[correct_card] = 'A'
    ascii_cards(card_display_list)
    global player_money
    player_money -= int(amount)
    print(f'"Oooh, tough luck that time. Have another go."\n\nYou lost {amount} dollars.')
    pause(3)


# this is the round loop
def card_picking_loop():
    """Loop that displays the cards' backs, fronts, then shuffles them around,
    makes the player pick one, and determines if that was the correct pick."""
    while True:
        correct_card = random.randint(0, 2)
        card_display_list = [' ', ' ', ' ']
        ascii_cards_backs()
        pause(2)
        card_display_list[correct_card] = 'A'
        ascii_cards(card_display_list)
        print('''"Here's the Ace. Follow its movements."''')
        input('\nPress return key when ready.')
        correct_card = card_shuffle(correct_card)
        player_guess = input('\n"Which card is the Ace?" [enter l for left, m for middle, or r for right] ')
        if player_guess.lower() in ['l', 'm', 'r']:
            card_display_list = ['l', 'm', 'r']
            if player_guess.lower() == card_display_list[correct_card]:
                win_round(amount_to_bet, correct_card)
                break
            else:
                lose_round(amount_to_bet, correct_card)
                break
        else:
            print('Pick a card with [l], [m], or [r].')
            pause(1)


#=============================================================================#

# Title screen
clear_screen()
print("\n\n\t\t\tThe game is Three Card Monty. ")
player_money = 100
pause(2)

# programme loop
while True:
    clear_screen()
    print_player_money(player_money)
    if player_money <= 0:
        print('\n"You broke, come back when you have more money. Sheeeeeeeet."\n')
        break
    participation = input('"Are you playing?" [y/n] ')
    if participation.lower() == 'y':
        while True:
            try:
                clear_screen()
                print_player_money(player_money)
                amount_to_bet = int(input('''"How much d'you want to bet?" [enter a number] '''))
                if amount_to_bet > player_money:
                    print('''"I need to see that cash first, don't bet what you don't have." ''')
                    pause(2)
                else:
                    break
            except ValueError:
                print('"You need to gimme a number to bet."')
                pause(2)
        print(f'"For {amount_to_bet} dollars, follow the Ace."')
        pause(2)
        card_picking_loop()
    elif participation.lower() == 'n':
        print('"Then move it along."\n')
        break
    else:
        print('\n"Huh? What was that?"')
        pause(1)
