# 
# Solution to Project Euler problem 10
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=10
# https://github.com/andreafresco/Project-Euler
#

def Is_prime(n): # check if the number n is prime
    
    assert n > 0
    
    i = 2
    
    # we restrict the search of prime numbers between 2 and sqrt(n)
    while i*i <= n: # equivalent to i <= sqrt(n)
        if n%i == 0:
            return False # if the number has a divisor then it's NOT prime
        i+=1
        
    return True # if no divisors were found then it's a prime number


def summation_of_primes(N_max):
    
    somma = 0 # init the sum to 0
    
    for i in range(2, N_max):
        
        if Is_prime(i):
            somma += i
    
    return somma
    

if __name__ == "__main__":
    
    print(summation_of_primes(2*10**6))
    # it gives the right result but it takes 10s - TO BE IMPROVED!
    