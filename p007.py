# 
# Solution to Project Euler problem 7
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=7
# https://github.com/andreafresco/Project-Euler
#

def Is_prime(n): # check 
    
    assert n > 0
    
    i = 2
    
    # we restrict the search of prime numbers between 2 and sqrt(n)
    while i*i <= n: # equivalent to i <= sqrt(n)
        if n%i == 0:
            return False # if the number has a divisor then it's NOT prime
        i+=1
        
    return True # if no divisors were found then it's a prime number
 
def IDXthPrime(idx):
    
    i = 2
    primeCounts = 0
    
    while primeCounts < idx:
        if Is_prime(i):    
            primeCounts+=1
        i += 1
    
    return i-1

if __name__ == "__main__":
    
    print(IDXthPrime(10001))
    