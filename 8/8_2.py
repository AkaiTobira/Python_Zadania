#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from math import sqrt
import cmath



def solve3(a,b,c):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    if a == 0:
	if b == 0:
		return None
	elif b != 0:
	    if c == 0:
		return 0
	    if c != 0:
		return (-c/b)
    elif a != 0:
	if b == 0:
	    if c == 0:
		return 0
	    if c != 0:
		if (a < 0 and c > 0) or (a > 0 and c < 0):
			return (sqrt(float(-c)/float(a)),-sqrt(float(-c)/float(a)))
		if (a > 0 and c > 0) or (a < 0 and c < 0 ):
			temp = complex(c/a,1)
			return (cmath.sqrt(temp),-cmath.sqrt(temp))
	elif b != 0:
	     if c == 0:
		return (0,float(b)/float(a))
	     if c != 0:
		delta = b*b-4*a*c
		if delta > 0 :
			return ((-b-sqrt(delta)/2*a),(-b+sqrt(delta)/2*a) )
		elif delta < 0 :
			temp = complex(delta,1)
			return ((-b-cmath.sqrt(delta)/2*a),(-b+cmath.sqrt(delta)/2*a))
		else :
			return -b/(2*a)




for i in range(-15,16,1):
	for j in range(-15,16,1):
		for k in range(-15,16,1):
			print i,j,k, solve3(i,j,k)
			

print solve3(-2,2,-2)
