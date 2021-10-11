# 
# Solution to Project Euler problem 12
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=12
# https://github.com/andreafresco/Project-Euler
#

def find_n_divisors(n): # find number of divisors
    
    
    n_divisors = 0 # init n_dividers to 0
    i = 1
    
    while i*i <= n: # We loop until sqrt(n) finding only half of the divisors
                    # the other half will be equal to n / i_th_divisor.
                    # Therefore every time we find a divisors we count it as two.
                    # If the number is a squared number we will have the same 
                    # divisor with multiplicity 2 and thus we have to remove 1
                    # to the number of divisors we found.
        
        if n%i==0:
            n_divisors += 2 
        i += 1
            
    i -= 1 # remove the last update to get the last value checked by the while
    # loop
    
    if i**2==n: # if the last value is the sqrt of the initial number we have a 
        # doble divisors (e.g. 4 = 2*2 -> in this case 2 will have multiplicity equal to 2)
        n_divisors -= 1
              
    return n_divisors 

def highly_divisible_triangular_number(n_lim):
    
    i = 2
    triangular_num = 1
    
    while find_n_divisors(triangular_num) < n_lim:
        triangular_num += i
        i+=1
        
    return triangular_num

if __name__ == "__main__":
    
    print(highly_divisible_triangular_number(500))
    