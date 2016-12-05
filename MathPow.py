#!/usr/bin/env python
from __future__ import division	#Because python 2.7 division sucks
import pytest

def pow(base,exponent):
	result=1.0
	for i in range(0,abs(exponent)):
		if exponent>=0:
			result=result*base
		else:
			result=result/base
	return result

def test_pow():
	assert pow(2,2)==4.0
	assert pow(10,-2)==0.01
	assert pow(1000,1)==1000.0
	assert pow(1000,0)==1.0
