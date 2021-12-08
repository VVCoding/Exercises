# Author: Vedant Vohra
# Date: 2021-11-16
# Description: An in-class python exercise

# Coin Flips
# This problem was asked by Microsoft.
# You have n fair coins and you flip them all at the same time. 
# Any that come up tails you set aside. 
# The ones that come up heads you flip again. 
# How many rounds do you expect to play before only one coin remains?
# Write a function that, given n, 
# returns the number of rounds you'd expect to play until one coin remains.

import random
def CoinFlips(ncoins_):
    choices = ['H','T']
    
    numb_coins = ncoins_
    numb_rounds = 0
    while numb_coins > 1:
        
        # count the number of rounds we do
        numb_rounds +=1
        
        # flip the coins
        flip_list = []
        for n in range(numb_coins):
            flip = random.choice(choices)
            flip_list.append(flip)
            
        # remove the tails
        numb_coins = sum([1 for x in flip_list if x == 'H'])
        
    return numb_rounds

x = CoinFlips(100)
print(x)