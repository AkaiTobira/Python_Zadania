#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from random import randint


class Stack:

	def __init__(self, size=10):
		self.items = size * [0]      # utworzenie tablicy
		self.takeALook = size * [False]
		self.n = 0                      # liczba elementów na stosie
		self.size = size

	def is_empty(self):
		return self.n == 0

	def is_full(self):
		return self.size == self.n

	def push(self, data):
		if data > self.items:
			raise ValueError
		if not self.takeALook[data]:  
			self.items[self.n] = data
			self.takeALook[data] = True
			self.n = self.n + 1
		else :
			return

	def pop(self):
		self.n = self.n - 1
		data = self.items[self.n]
		self.takeALook[data] = False
		self.items[self.n] = 0    # usuwam referencję
		return data

S = Stack(50)

for i in range(50000):

	for i in range(S.size-1):
		k = randint(0,i+1)
		S.push(k)
		print k,
		
	print ""

	while not S.is_empty():
		print S.pop(),
	
