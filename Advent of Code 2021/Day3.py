# Author: Vedant Vohra
# Date: 12/21/21
# Description: Advent of Code day 3 exercise

# Load Data
import csv

def LoadInputFile():
    with open('/Users/gvohra/Development/Advent of Code/day3data.txt') as data_file:
        reader = csv.reader(data_file)
        
        input_list = []
        for row in reader:
            input_list.append(int(row[0]))
            
        return input_list
    
print(LoadInputFile())

# Day 3 Part 1
