# 
# Solution to Project Euler problem 16
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=16
# https://github.com/andreafresco/Project-Euler
#

def sum_of_digits(power): # BRUTE FORCE
    
    number = 2**power
    somma = 0
    
    while number % 10 != 0 or number // 10 != 0:
        somma += number % 10
        number //= 10
    return somma


if __name__ == '__main__':
    
    print(sum_of_digits(1000))
    