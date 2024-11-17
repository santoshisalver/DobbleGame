# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 06:30:58 2024

@author: santo
"""
# Importing required modules
import string
import random

# Initialize an empty list for storing possible characters
symbols = []
# Add all letters (both lowercase and uppercase) from ASCII to the list
symbols = list(string.ascii_letters)

# Initialize two lists to represent the two "cards"
card1 = [0] * 5  # Card 1 will have 5 positions initialized to 0
card2 = [0] * 5  # Card 2 will also have 5 positions initialized to 0

# Randomly choose positions for the similar symbol on both cards
pos1 = random.randint(0, 4)  # Random index between 0 and 4 for card1
pos2 = random.randint(0, 4)  # Random index between 0 and 4 for card2

# Choose a random symbol (letter) to be shared between the cards
samesymbol = random.choice(symbols)
# Remove the selected symbol from the list of available symbols
symbols.remove(samesymbol)

# If the positions are the same, place the same symbol in both cards at the same position
if pos1 == pos2:
    card2[pos1] = samesymbol
    card1[pos1] = samesymbol
else:
    # Place the symbol at the selected positions in both cards
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol

    # Fill in random symbols at other positions, ensuring they don't repeat the same symbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])  # Remove the newly chosen symbol from the list
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])  # Remove the newly chosen symbol from the list

# Initialize a counter to iterate through the positions of the cards
i = 0
while i < 5:
    if i != pos1 and i != pos2:  # Skip the positions that already have the same symbol
        # Choose a random symbol for card1 and card2 at the current position
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)  # Remove this symbol from the available list
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)  # Remove this symbol from the available list

        # Place the chosen symbols in the current positions on both cards
        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1  # Move to the next index

# Print the final cards for the user to see
print(card1)
print(card2)

# Prompt the user to spot the symbol that is the same on both cards
ch = input("Spot the similar symbol: ")

# Check if the user entered the correct symbol and provide feedback
if ch == samesymbol:
    print("Right")  # Correct answer
else:
    print("Wrong")  # Incorrect answer
    print(f"The correct symbol was: {samesymbol}")  # Reveal the correct symbol
