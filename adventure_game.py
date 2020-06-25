import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    # Opening text for the game.
    print_pause("You find yourself standing on a sunny beach in Venezuela.")
    print_pause("The country is in crisis and you are here to stabilize things.")
    print_pause("Before you is a jungle and rock to your right.")

def jungle(action):
    # Actions that take place as you the jungle and encounter the police.
    print_pause("You decide to walk through the jungle.")
    print_pause("Upon walking a few feet in, you hear footsteps in the distance.")
    print_pause("It's the National Police!")
    print_pause("They're here to take you!")
    action = input("What will you do? (1) Fight or (2) Escape\n")
    if action == '1':
        fight(weapons)
    elif action == '2':
        print_pause("You escape into the jungle. Luckily, no one is pursuing you.")
        choices()
    else:
        print_pause("Sorry, I don't understand. Please enter 1 or 2.")
        choices()

def rock(action):
    # You explore the rock to see what's there.
    if "player_weapon" in weapons:
        print_pause("You approach the rock.")
        print_pause("The rock has nothing as you've already taken what's there.")
        print_pause("You return to the beach.")
        choices()
    else:
        print_pause("You decide to check out the rock.")
        print_pause("It's not very big; only a few hundred pounds heavy.")
        print_pause("On it is an 'player_weapon'. ")
        print_pause("You take it and return to the beach.")
        items.append("player_weapon")
        choices()

def fight(items):
    #
    if "player_weapon" in weapons:
        print_pause("As the Police move to arrest you, you hoist your 50 caliber gun for assault.")
        print_pause("With your barrels blazing, you obliterate the ban of thugs.")
        print_pause("Venezuela isn't free, but you sure shook things up for Maduro and his cronies.")
        print_pause("Mission success.")
        play_again()
    else:
        print_pause("You draw your pistol to fight.")
        print_pause("No good. The police arrest you.")
        print_pause("Mission failed")
        play_again()

def choices():
    print_pause("Enter 1 to enter the jungle.")
    print_pause("Enter 2 to check out the rock.")
    action = input("What would you like to do?\n")
    if action == '1':
        jungle(weapons)
    elif action == '2':
        rock(weapons)
    else:
        print_pause("Sorry I don't understand. Please enter 1 or 2.")

def play_again():
    # The code that enables the player to decide whether to play the game again.
    request = input("Would you like to play again? (y/n)")
    if "y" in request:
        print_pause("Excellent! Restarting the game!")
        play_game()
    elif "n" in request:
        print("Thanks for playing!")
        exit()
    else:
        print_pause("Invalid input. Please choose y or n.")

def play_game():
    intro()
    choices()
    jungle(action)
    fight(weapons)
    rock(choices)
    play_again()

    weapons = ["50 caliber gun", "M16", "AR-15"]
    weapon = random.choice(weapons)

play_game()
