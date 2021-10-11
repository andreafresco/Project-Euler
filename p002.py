# 
# Solution to Project Euler problem 2
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=2
# 

def EvenFibonacciNumbers(N):
    
    x_n_1 = 1
    x_n = 1
    somma = 0 # init the sum to 0
    
    while somma < N:
        
        # Keeping track of the last two numbers
        # x[n-1]: x_n_1 -> previous Fibonacci number 
        # x[n]: x_n -> current Fibonacci number
        
        temp = x_n # temporary variable for swapping 
        x_n += x_n_1
        x_n_1 = temp
        
        if x_n%2 == 0:
            somma += x_n #sum of even value terms
            
            
    return somma


if __name__ == "__main__":
    
    print(EvenFibonacciNumbers(4 * 10**6))