#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from random import randint

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    x = 0.0
    y = 0.0
    nk = 0
    for i in range(n):
	x = (float(randint(0,92233720))/float(92233720))*2.0 - 1.0
	y = (float(randint(0,92233720))/float(92233720))*2.0 - 1.0
	#print x,y
	if x**2 + y**2 <= 1:
	     nk += 1

    return 4.0*float(nk)/n

   

print calc_pi(1000000)
