#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from random import randint

def linearSentinelSearch( L, item , start=0 ):
	lon = len(L)-1
	if start > lon:
		return -1
	last = L[lon]
	L[lon] = item;
	i = start;
	while(L[i] != item):
		i+=1
	L[lon] = last;
	
	if i < lon or item == L[lon]:
		return i
	else :
		return -1
	
	
def buitList( leng, maxi, mini ):
	L = [];
	for i in range(leng) :
		L.append(randint(mini,maxi))
	return L;

def occurence( L, item ):
	if len(L) == 0 :
		return [-1];
	R = [];
	for i in range(len(L)):
		k = linearSentinelSearch(L,item,i)
		if k == -1 :
			if len(R) == 0 :
				return [-1];
			return R
		else:
			if k not in R :
				R.append(k)
		i = R[len(R)-1]
	return R
	
	
	


print occurence(buitList(100,10,0), 3)
print occurence( [2,3,4,2,3,5,2,3,1,3,5,2,3,4,5], -100 );
print occurence( [], 12 );