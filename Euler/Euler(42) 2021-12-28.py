# Author: Vedant Vohra
# Date: 2021-12-28
# Description: Some in class Euler problems

# Euler problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
import math
import csv

def LoadInputFile():
    with open('/Users/gvohra/Development/Exercises/Euler42.txt') as input_file:
        reader = csv.reader(input_file)
        row = reader.__next__()
    return row
# for word in list_of_words:    
#    print(word)

# Euler Problem 42

# Function to translate word in to its numeric value
def TranslateWord(word_):
    value = 0
    for letter in word_:
        value += ord(letter) - 64
    
    return value

def TriangleSolve(tn_):
    return(math.sqrt(1+8*tn_)-1)/2

# Main Function
def Problem42():
    
# Some Variables/ Load Input File
    list_of_words = LoadInputFile()
    triangle_count  = 0
    
    # Using translate function and get numeric value
    for word in list_of_words:
       value = TranslateWord(word)
       
       solution = TriangleSolve(value)
       if solution.is_integer() == True:
           triangle_count += 1
    
    return triangle_count

print(Problem42())
                
        