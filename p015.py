# 
# Solution to Project Euler problem 15
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=15
# https://github.com/andreafresco/Project-Euler
#

import math

def binomial(n, k):
    
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

def n_of_routes(n):
    
    return binomial(2*n, n)

if __name__ == "__main__":
    
    print(n_of_routes(20))
    