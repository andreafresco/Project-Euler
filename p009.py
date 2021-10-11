# 
# Solution to Project Euler problem 9
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=9
# https://github.com/andreafresco/Project-Euler
#

def SpecialPythagoreanTriplet():
    
    # Let's define a, b as catheti and c as hypotenuse
    # According to the triangular inequality: a + b < c (1)
    # Given by the problem: a + b + c = 1000 (2)
    # By combining (1) and (2), we obtain that c < 500
    
    for c in range(500):
        for b in range(500):
            a = 1000 - b - c
            if a**2 + b**2 == c**2:
                print('Pythagorean triplet: '+ str(a) + ' ' + str(b) + ' ' + str(c))
                return a*b*c
    return -1
    

if __name__ == "__main__":
    
    print(SpecialPythagoreanTriplet())
    