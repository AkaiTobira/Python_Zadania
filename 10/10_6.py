#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from Queue import PriorityQueue

class PriorityQueImprove(PriorityQueue):

	def __len__(self):
		return len(self.queue)
	
	def __str__(self):
		return str(self.queue)
  
	def increase(self, value):
		K = []
		Z = self.get()
		if isinstance( Z, (int, long, float)):
			K.append(Z - value)
			while len(self.queue) != 0:
				Z = self.get()
				K.append(Z - value)
			self.queue = K
		else :
			K.append((Z[0] - value,) + Z[1:len(Z)])
			while len(self.queue) != 0:
				Z = self.get()
				K.append( (Z[0] - value,) + Z[1:len(Z)])
			self.queue = K  
  
  
Pr = PriorityQueImprove()
 
Pr.put((72,1))
Pr.put((-2,1))
Pr.put((61,1))
Pr.put((322,1))
Pr.put((8,1))
Pr.put((35,1))
Pr.put((1,1))
Pr.put((6,1))
  
print str(Pr)
Pr.increase(7)
print str(Pr)