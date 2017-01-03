#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from random import randint

def randomManyMultiply( leng,mini,maxi):
	W = randint(mini,maxi)
	L = [];
	for i in range(leng) :
		if randint(mini,maxi) > (mini+maxi)/2 :
			L.append(randint(mini,maxi))
		else :
			L.append(W);
	return L;


def liderSearch( L ):
	D = {}
	for item in L:
		if D.has_key(item):
			k = D[item]
			del D[item]
			D[item] = k+1
		else:
			D[item] = 1
	

	for item in L:
		if D[item] >= (len(L)/2 + 1):
			P = {}
			P[item] = D[item]
			return P
			
	return None;

print liderSearch( [1,3,4,3,2,1,1] )
print liderSearch( [1,2,2,3,3,3,3,2,3] )
print liderSearch( [2,3,1,1,1,4] )
print liderSearch( randomManyMultiply(500,0,100) )
