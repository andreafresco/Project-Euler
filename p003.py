# 
# Solution to Project Euler problem 3
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=3
# 

def IsPrime1(num):
    
   
    i = 2
    
    while i*i <= num:
        if num%i == 0:
            return False
        i += 1
        
    return True


if __name__ == "__main__":
    
    print(IsPrime1(5))