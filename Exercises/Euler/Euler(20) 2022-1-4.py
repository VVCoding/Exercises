# Author: Vedant Vohra
# Date: 1/4/2022
# Euler Problem 20
# Description   
    #n! means n × (n − 1) × ... × 3 × 2 × 1
    #For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    #And the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    #Find the sum of the digits in the number 100!

def Factorial(number):
    mult = 1
    for n in range(1,number):
        mult *= n
    return mult


def Problem20():
    Onehundred = Factorial(100)
    Onehundred = str(Onehundred)
    answer = 0
    for elt in Onehundred:
        elt = int(elt)
        answer += elt
    
    return answer

print(Problem20())