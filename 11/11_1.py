##!/usr/bin/python
# -*- coding: utf-8 -*-
#
import random
import math

def randomNoSort( size ):
	L = []
	for i in range(size):
		L.append(i)
	random.shuffle(L)
	return L
  
def randomAlmostSort( size ):
	L = []
	for i in range(size):
		L.append(i)
	
	
	for i in range(size-1):
		if random.random() > 0.5:
			L[i],L[i+1] = L[i+1],L[i] 
			
	return L
  
def randomReverseSort( size ):
	L = []
	for i in range(size-1,-1,-1):
		L.append(i)
	for i in range(size-1):
		if random.random() > 0.5:
			L[i],L[i+1] = L[i+1],L[i] 
			
	return L
  
def randomGauss( size ):
	L = []
	for i in range(size):
		k = random.gauss(0,size)
		while k in L:
			k = random.gauss(0,size)
		L.append(k)
	random.shuffle(L)
	return L
	
def randomMultiply( size ):
	L = []
	for i in range(size):
		L.append(random.randint(-int(math.sqrt(size) +1)+2,int(math.sqrt(size) +1)))
	random.shuffle(L)
	return L
 
print randomNoSort(12)
print randomAlmostSort(12)
print randomReverseSort(12)
print randomGauss(12)
print randomMultiply(12)