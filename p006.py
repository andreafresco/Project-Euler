# 
# Solution to Project Euler problem 6
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=6
# https://github.com/andreafresco/Project-Euler
#

def Sum_square_difference(n):
    somma = 0 # init sum = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            somma += i*j # make the products of only the upper triangular 
            # matrix elements
            
    return 2*somma



if __name__ == "__main__":
    
    print(Sum_square_difference(100))
    