# 
# Solution to Project Euler problem 1
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=1
# 

def multiples_of_3_or_5(N):
    
    return sum([i for i in range(N) if (i%3==0 or i%5==0)])


if __name__ == "__main__":
    
    print(multiples_of_3_or_5(1000))