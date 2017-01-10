##!/usr/bin/python
# -*- coding: utf-8 -*-
#

from random import randint
from random import gauss
from random import shuffle
import math

def randomNoSort( size ):
	L = []
	for i in range(size):
		L.append(i)
	shuffle(L)
	return L
  
def randomAlmostSort( size ):
	L = []
	for i in range(size):
		L.append(i)
	
	
	k = randint(0,size)
	for i in range(size-1):
		j = randint(0,size)
		if k > j:
			p = i+randint(0,1)
			temp = L[i]
			L[i] = L[p]
			L[p] = temp
	return L
  
def randomReverseSort( size ):
	L = []
	for i in range(size-1,-1,-1):
		L.append(i)
	k = randint(0,size)
	for i in range(size-1):
		j = randint(0,size)
		if k > j:
			p = i+randint(0,1)
			temp = L[i]
			L[i] = L[p]
			L[p] = temp
	return L
  
def randomGauss( size ):
	L = []
	for i in range(size):
		k = gauss(0,size)
		while k in L:
			k = gauss(0,size)
		L.append(k)
	shuffle(L)
	return L
	
def randomMultiply( size ):
	L = []
	for i in range(size):
		L.append(randint(-int(math.sqrt(size) +1)+2,int(math.sqrt(size) +1)))
	shuffle(L)
	return L
 
print randomNoSort(12)
print randomAlmostSort(12)
print randomReverseSort(12)
print randomGauss(12)
print randomMultiply(12)