# 
# Solution to Project Euler problem 3
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=3
# https://github.com/andreafresco/Project-Euler
#
    
def smallest_prime(n): # return the smallest prime of n or n itself
    # if it is prime
    
    assert n > 0
    
    i = 2
    
    # we restrict the search of prime numbers between 2 and sqrt(n)
    while i*i <= n: # equivalent to i <= sqrt(n)
        
        if n%i == 0:
            return i # we return the first prime number we encounter
        
        i+=1
        
    return n


def Largest_Prime_Factor(P):
    
    smallest = smallest_prime(P) # finding the smallest prime
    
    while smallest < P: 
        
        # Dividing the number by all it's smallest prime numbers until we reach
        # the highest prime number (condition: P = smallest)
        P //= smallest # integer division to avoid floating point results (e.g. 17.0 instead of 17)
        smallest = smallest_prime(P)
        
    return P
    

if __name__ == "__main__":
    
    print(Largest_Prime_Factor(600851475143))
    