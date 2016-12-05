#!/usr/bin/python
# -*- coding: utf-8 -*-
#


def odwracanie ( L,left,right ):
	"""Fukncja odwracajaca liste L, od indexu left do right włacznie"""
	if left > right or right >= len(L) or left >= len(L):
		return L
	L[left], L[right] = L[right], L[left]

	if (right - left)/2 == 0:
		return L
	else:
		return odwracanie(L,left+1, right-1)

L = [1,2,3,4,5,6,7,8,9,10,11]
print L				# [1,2,3,4,5,6,7,8,9,10,11]
print odwracanie ( L , 2, 7 )   # [1,2,8,7,6,5,4,3,9,10,11]


def reverse( L, left, right):
	"""Fukncja odwracajaca liste L, od indexu left do right włacznie"""
	if left > right or right >= len(L) or left >= len(L):
		return L
	k = 0
	for i in range( left,(right+left+1)/2,1):
			L[i], L[right-k] = L[right-k], L[i]
			k+=1

	return L


L = [1,2,3,4,5,6,7,8,9,10,11]
print L	                       # [1,2,3,4,5,6,7,8,9,10,11]
print reverse ( L , 3, 6 )     # [1,2,3,7,6,5,4,8,9,10,11]
			