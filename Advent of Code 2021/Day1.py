# Author: Vedant Vohra
# Date: 12/7/21
# Description: Advent of Code day 1 exercise

# Load Data
import csv

def LoadInputFile():
    with open('/Users/gvohra/Development/Advent of Code/day1data.txt') as data_file:
        reader = csv.reader(data_file)
        
        input_list = []
        for row in reader:
            input_list.append(int(row[0]))
            
        return input_list
    
# print(LoadInputFile())

# Part 1
def AdventofCodeDay1Part1():
    count = 0
    data = LoadInputFile()
    lesser = 0
    for x in data[1:]:
            if x > lesser:
                count += 1
            lesser = x
                
    return count - 1
            
print(AdventofCodeDay1Part1())

# Part 2
def AdventofCodeDay1Part2():
    data = LoadInputFile()
    prev_window = 0
    count = 0
    for idx in range(2,len(data)):
        curr_window = data[idx] + data[idx-1] + data[idx-2]
        
        if prev_window < curr_window:
            count += 1
        prev_window = curr_window
        
    return count-1
            
print(AdventofCodeDay1Part2())



        
       
