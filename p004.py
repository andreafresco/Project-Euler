# 
# Solution to Project Euler problem 4
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=4
# https://github.com/andreafresco/Project-Euler
#
    
def IsPalindrome(num):
    
    num_str = str(num)
    
    N = len(num_str)
    
    if N%2 == 0: # even
        
        for i in range(N//2):
            if num_str[i] != num_str[N-1-i]:
                return False
        return True
        
    else: # odd
        
        for i in range(N//2+1):
            if num_str[i] != num_str[N-1-i]:
                return False
        return True
        
def LargestPalindromeProduct(n):
    
    largest = 1
    
    for i in range(n):
        for j in range(n):
            prod = i*j
            if IsPalindrome(prod) and prod > largest:
                largest = prod
    return largest

    

if __name__ == "__main__":
    
    print(LargestPalindromeProduct(1000))
    