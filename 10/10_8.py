#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from random import randint

class RandomQueue:

	def __init__(self, size = 10): 
		self.queue = []
		self.size = size

	def __str__(self):
		return str(self.queue)

	def insert(self, item): 
		if len(self.queue) < self.size:
			self.queue.append(item)

	def remove(self):    # zwraca losowy element
		i = randint(0,len(self.queue)-1) 
		j = self.queue[i]
		self.queue[i] = self.queue[len(self.queue)-1]
		del self.queue[len(self.queue)-1]
		return j
	

	def is_empty(self): 
		return len(self.queue) == 0

	def is_full(self): 
		return self.size == len(self.queue)
	
	
	
	

R = RandomQueue(20)
for i in range(20):
	R.insert(i)
print R
while not R.is_empty():
	R.remove()
	print R
