# Python Test for Advanced Students
# Author: Vedant
# Date: 1/25/2022
# Description:  A collection of small programming questions
# used to test a students ability to use the Python programming
# language to solve problems.

# Question 1 ----------------------------------------------
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

##Input: nums = [2,7,11,15], target = 9
##Output: [0,1]

def Question1(nums,target):
    for elt in nums:
        for i in nums:
            if elt + i == target:
                answer = [nums.index(elt), nums.index(i)]
                
                return answer

nums1= [2,7,11,15]
target1 = 17
print(Question1(nums1, target1))

# Question 2 ----------------------------------------------
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.

##Input: x = 121
##Output: true

def Question2(x):
    x1 = str(x)
    x2 = x1[::-1]
    if x1 == x2:
        return True
    else:
        return "You did not pick a palindrome"

print(Question2(121))

# Question 3 ----------------------------------------------
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.

##Input: s = "()[]{}"
##Output: true

##Input: s = "(]"
##Output: false

# Question 4 ----------------------------------------------
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

##Input: nums = [1,2,3,1]
##Output: true

def Question4(nums):
    return len(nums) == len(set(nums))
nums = [1,2,3,1]
print(Question4(nums))

# Question 5 ----------------------------------------------
# There is a robot starting at the position (0, 0), the origin, on a 2D plane. 
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. 
# Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

##Input: moves = "UD"
##Output: true

##Input: moves = "LL"
##Output: false

def Question5(moves):
    Llist = 0
    Ulist = 0
    Dlist = 0
    Rlist = 0
    for letter in moves:
        if letter == 'L':
            Llist += 1
        if letter == 'R':
            Rlist += 1
        if letter == 'U':
            Ulist += 1
        if letter == 'D':
            Dlist += 1
            
    return Llist == Rlist and Ulist == Dlist

moves = "LRUDLRUDLRUDLRUDLRUDUD"
print(Question5(moves))



            