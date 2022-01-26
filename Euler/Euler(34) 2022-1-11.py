# Author: Vedant Vohra
# Date: 1-11-2022
# Description: Euler problem 34

# Euler Problem 34
    # 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    # Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    # Note: As 1! = 1 and 2! = 2 are not sums they are not included

def Euler1():
    sum = 0
    for elt in range(1,1000):
        if elt % 3 ==0:
            sum += elt  
        if elt % 5 ==0:
            sum += elt
        if elt % 15 == 0:
            sum -= elt
    return sum
    
print(Euler1())

def Euler13():
    sum2 = 0
    x = 2**1000
    for elt in str(x):
        sum2 += int(elt)  
    
    return sum2  

print(Euler13())

def Euler48():
    answer = 0
    sum3 = 0
    for elt in range(1,1001):
        sum3 += elt**elt
    x = str(sum3)
    return x[-10:]
print(Euler48())

def Euler6():
    sum1 =0
    sum2 =0
    for elt in range (1,101):
        sum1 += elt**2
    for elt in range (1,101):
        sum2 += elt
    
    return sum2**2-sum1
print(Euler6())

def Euler9():
    for a in range(1,1001):
        for b in range(1,1001):
            for c in range(1,1001):
                if a**2 + b**2 == c**2:
                    if a+b+c == 1000:
    
                        return a*b*c
print(Euler9())

def Factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    
    return factorial
        

def Euler34():
    answer = 0
    sum_group = []
    for elt in range(10,2540161):
        sum1 = 0
        for elt2 in str(elt):
            sum1 += Factorial(int(elt2))
        if sum1 == elt:
            answer += sum1
            sum_group.append(elt)
            print('Found a number', elt)
    return sum(sum_group)

print(Euler34())


                
            
            

