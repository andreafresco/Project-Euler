# 
# Solution to Project Euler problem 17
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=17
# https://github.com/andreafresco/Project-Euler
#

first_twenty = {
0: '',
1:  'one',
2:	'two',
3:	'three',
4:	'four',
5:	'five',
6:	'six',
7:	'seven',
8:	'eight',
9:	'nine',
10:	'ten',
11:	'eleven',
12:	'twelve',
13:	'thirteen',
14:	'fourteen',
15:	'fifteen',
16:	'sixteen',
17:	'seventeen',
18:	'eighteen',
19:	'nineteen',
20:	'twenty',
30: 'thirty',
40: 'forty',
50: 'fifty',
60: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
100: 'hundred',
1000: 'thousand'
    }


def count_letters(num):
    
    somma = 0 # initialize a variable that will contain the sum
    rest = num % 100 # find the tens
    
    if  rest <= 20: # if the tens are below 20 then we have special cases 
        somma += len(first_twenty[rest])
        
    else: # otherwise the number construction is modular: the tens + the least significant digit
        somma += len(first_twenty[((num//10)%10)*10]) + len(first_twenty[num%10])
        
    num //= 100 # trim the tens from the original number and analyse the hundreds
    
    if num%10 > 0: # if the original number was above hundreads
        somma += len(first_twenty[num%10]) + len(first_twenty[100])
        if rest != 0: # if the number is not 100, 200, 300 and so on, add the 'and' length
            somma += len('and')
            
    num //= 10 # trim the hundreads
    
    if num > 0: # if the the resulting number has still some digit left, it means that
        # the original number was above 1000
        somma += len(first_twenty[1]) + len(first_twenty[1000]) # then add 'one' + 'thousand'
    
    return somma

def compute_count_letters(N):

    somma = 0
    for i in range(N+1):
        
        somma += count_letters(i)
    
    return somma

if __name__ == '__main__':
    
    print(compute_count_letters(1000))
    