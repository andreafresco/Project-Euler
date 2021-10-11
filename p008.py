# 
# Solution to Project Euler problem 8
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=8
# https://github.com/andreafresco/Project-Euler
#

def Largest_product_in_a_series(filename, n_adj_digit): # n_adj_digit: 
    # number of adjacent digits_
    with open(filename) as f:
        content = f.readlines()    
    
    prod = 0
    string_max = ''
    string_final = ''
    for i in range(len(content)):
        string = content[i].replace('\n', '')
        string_final+=string
    
    
    for j in range(len(string_final) - n_adj_digit + 1):
        temp_string = string_final[j:j+n_adj_digit]
        temp_prod = 1
        for k in temp_string:
            temp_prod *= int(k)
        if temp_prod > prod:
            prod = temp_prod
            string_max = temp_string
            
    return prod     


if __name__ == "__main__":
    
    print(Largest_product_in_a_series(r"./data/Prob008.txt", 13))
    