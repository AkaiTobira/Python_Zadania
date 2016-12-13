#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from Queue import PriorityQueue

class PriorityQueImprove(PriorityQueue):
	#TODO
	def __len__(self):
		return len(self.queue)
		
  
	def increase(self, value):
		K = PriorityQueImprove()
		Z = self.get()
		if isinstance( Z, (int, long, float)):
			K.put(Z - value)
			while len(self) != 0:
				Z = self.get()
				K.put(Z - value)
			self = K
		else :
			K.put((Z[0] - value,) + Z[1:len(Z)])
			while len(self) != 0:
				print "KKKK"
				Z = self.get()
				print Z[0]
				K.put( (Z[0] - value,) + Z[1:len(Z)])
			self = K
  
  
  
Pr = PriorityQueImprove()
 
Pr.put((72,1))
Pr.put((-2,1))
Pr.put((61,1))
Pr.put((322,1))
Pr.put((8,1))
Pr.put((35,1))
Pr.put((1,1))
Pr.put((6,1))
  

Pr.increase(7)
  
  
print Pr.get(),
print Pr.get()
  