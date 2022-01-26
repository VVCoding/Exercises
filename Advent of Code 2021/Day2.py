# Author: Vedant Vohra
# Date: 12/14/21
# Description: Advent of Code day 2 exercise

# Load Data
import csv

def LoadInputFile():
    with open('/Users/gvohra/Development/Advent of Code/day2data.txt') as data_file:
        reader = csv.reader(data_file)
        
        input_list = []
        for row in reader:
            input_list.append((row[0].split()[0], int(row[0].split()[1])))
            
        return input_list

# print(LoadInputFile())

# Part 1
def AdventofCodeDay2Part1():
    data = LoadInputFile()
    vertical = 0
    horizontal = 0
    for x,y in data:
        if x == 'forward':
            horizontal += y
        if x== 'down':
            vertical += y
        if x== 'up':
            vertical -= y
        
    return horizontal*vertical

print(AdventofCodeDay2Part1())

# Part 2
def AdventofCodeDay2Part2():
    data = LoadInputFile()
    aim = 0
    depth = 0
    horizontal = 0
    for x,y in data:
        if x == 'forward':
            horizontal += y
            depth += aim*y
        if x== 'down':
            aim += y
        if x== 'up':
            aim -= y
        
    return horizontal*depth

print(AdventofCodeDay2Part2())