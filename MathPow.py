#!/usr/bin/env python
from __future__ import division	#Because python 2.7 division sucks

def pow(base,exponent):
	result=1.0
	for i in range(0,abs(exponent)):
		if exponent>=0:
			result=result*base
		else:
			result=result/base
	return result
	