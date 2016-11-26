#!/usr/bin/python
# -*- coding: utf-8 -*-
#


def odwracanie ( L,left,right ):
	"""Fukncja odwracajaca liste L, od indexu left do right włacznie"""
	if left > right or right >= len(L) or left >= len(L):
		return
	
	g = len(L)
	for i in range(left):
			L.append(L[i])
	
	for i in range(right,left-1,-1):
			L.append(L[i])

	for i in range(right +1, g, 1):
			L.append(L[i])
	del L[0:g]
	return L

L = [1,2,3,4,5,6,7,8,9,10]
print odwracanie ( L , 0, 9 )   # [10,9,8,7,6,5,4,3,2,1]
print L				# [10,9,8,7,6,5,4,3,2,1]

def s2( L, left, right):
	"""Fukncja odwracajaca liste L, od indexu left do right włacznie"""
	if left > right or right >= len(L) or left >= len(L):
		return
	
	g = list()
	for i in range( right,left-1,-1):
			g.append(L[i])
	return g


L = [1,2,3,4,5,6,7,8,9,10]
print s2 ( L , 3, 6 )   
print L				