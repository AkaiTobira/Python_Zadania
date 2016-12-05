#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from math import sqrt

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a+b>=c and a+c>=b and b+c>=a:
	p = float(a+b+c)*0.5
	R = sqrt(p*(p-a)*(p-b)*(p-c))
	return R
    else:
	raise ValueError

print heron(254,123,152)
