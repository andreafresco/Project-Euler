# 
# Solution to Project Euler problem 5
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=5
# https://github.com/andreafresco/Project-Euler
#
    
def GCD(a,b): # Greatest common divisor with EULER FORMULA
    
    while a!=b:
        if a>b:
            a = a-b
        if b>a:
            b = b-a
    return a

  
def mcm(a,b): # minimum common multiple
    return a*b//GCD(a,b)

def SmallestMultiple(N_max):

    prod = 1
    for i in range(1, N_max+1):
        prod = mcm(prod, i) # minimum common multiple of all the numbers
        # between 1 and N_max
    return prod 

if __name__ == "__main__":
    
    print(SmallestMultiple(20))
    