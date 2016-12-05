#!/usr/bin/env python
def isPalindrome(inputString):
	n=len(inputString)
	for i in range(0,n/2):
		if inputString[i] != inputString[n-i-1]:
			return False
	return True
