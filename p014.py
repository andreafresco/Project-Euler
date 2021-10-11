# 
# Solution to Project Euler problem 14
# Copyright (c) Andrea Fresco. All rights reserved.
# 
# https://projecteuler.net/problem=14
# https://github.com/andreafresco/Project-Euler
#

import sys

class memoize:
	
	def __init__(self, func):
		self.func = func
		self.cache = {}
	
	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val

@memoize
def collatz_chain_length(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return collatz_chain_length(y) + 1    

def longest_chain():
    
	sys.setrecursionlimit(3000)
	longest = max(range(1, 1000000), key=collatz_chain_length)
	return longest


if __name__ == "__main__":
    
    print(longest_chain())
    