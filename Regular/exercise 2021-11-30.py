# Author: Vedant Vohra
# Date: 2021-11-30
# Description: Some in-class exercises

# Exercise 1
    # Divide Two Integers
    # Given two integers dividend and divisor, 
    # Divide two integers without using multiplication, division, and mod operator.
    # The integer division should truncate toward zero,which means losing its fractional part. 
    # For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
    # Return the quotient after dividing dividend by divisor.

def IntegerDivide(x,y):
    amount = 0
    const_x = x
    if const_x == 0:
        return 0 
    if y == 0:
        print('Nice try Buddy')
    while abs(x) >= y:
        x = abs(x)-y
        if const_x <0:
            amount -= 1
        if const_x>0:
            amount += 1
    
    return amount

z = IntegerDivide(-20,6)
print(z)

# Exercise 2
    # Large Integer
    # You are given a large integer represented as an integer array digits, 
    # Where each digits[i] is the ith digit of the integer. 
    # The digits are ordered from most significant to least significant in left-to-right order. 
    # The large integer does not contain any leading 0's.
    # Increment the large integer by one and return the resulting array of digits.
    
def LargeInteger(l1):
    l2 =[]
    str_num = ''
    for elt in l1:
        str_num += str(elt)
    
    y = int(str_num)
    z = y + 1
    e = str(z)
    for dig in e:
        l2.append(int(dig))
    return l2

l1 = [3,9,9]
a = LargeInteger(l1)
print(a)

# Homework assigned 2021-11-30
    # Best Time to Buy and Sell Stock
    # You are given an array prices where prices[i] is the price of a given stock on the ith day.
    # You want to maximize your profit by choosing a single day to buy one stock 
    # And choosing a different day in the future to sell that stock.
    # Return the maximum profit you can achieve from this transaction. 
    # If you cannot achieve any profit, return 0.
 
def Buy_Sell(l1):
    max_y =0
    for elt in l1:
        for x in l1:
            l1.index(x) < l1.index(elt)
            l1.index(x) >0
            l1.index(elt) >0
            if l1[l1.index(x)] < l1[l1.index(elt)]:
                y = l1[l1.index(elt)] - l1[l1.index(x)]
                if max_y < y:
                    max_y = y
    
    return max_y

l33 = [1,0,6,7,4]
x = Buy_Sell(l33)
print(x)
                
            

