#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from random import randint
from random import gauss
from random import shuffle
import math

def randomNoSort( l ):
	L = []
	for i in range(l):
		L.append(i)
	shuffle(L)
	return L
  
def randomAlmostSort( l ):
	L = []
	for i in range(l):
		L.append(i)
	
	
	k = randint(0,l)
	for i in range(l-1):
		j = randint(0,l)
		if k > j:
			p = i+randint(0,1)
			temp = L[i]
			L[i] = L[p]
			L[p] = temp
	return L
  
def randomReverseSort( l ):
	L = []
	for i in range(l-1,-1,-1):
		L.append(i)
	k = randint(0,l)
	for i in range(l-1):
		j = randint(0,l)
		if k > j:
			p = i+randint(0,1)
			temp = L[i]
			L[i] = L[p]
			L[p] = temp
	return L
  
def randomGauss( l ):
	L = []
	for i in range(l):
		k = int(gauss(0,l))
		while k in L:
			k = int(gauss(0,l))
		L.append(k)
	shuffle(L)
	return L
	
def randomMultiply( l ):
	L = []
	for i in range(l):
		L.append(randint(-int(math.sqrt(l) +1)+2,int(math.sqrt(l) +1)))
	shuffle(L)
	return L
 
print randomNoSort(12)
print randomAlmostSort(12)
print randomReverseSort(12)
print randomGauss(12)
print randomMultiply(12)