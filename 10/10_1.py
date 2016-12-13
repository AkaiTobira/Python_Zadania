#!/usr/bin/python
# -*- coding: utf-8 -*-
#


class Matrix:

	def __init__(self, rows=1, cols=1):
		self.rows = rows
		self.cols = cols
		self.data = [0] * rows * cols

	def __str__(self):
		st = ""
		for i in range(len(self.data)):
			st+=str(self.data[i]) + " "
			if (i+1)%self.cols == 0 :
				st+="\n"
			
		return st

	def __getitem__(self, pair):   # odczyt m[i,j]
		i, j = pair
		return self.data[i * self.cols + j]

	def __setitem__(self, pair, value):   # m[i,j] = value
		i, j = pair
		self.data[i * self.cols + j] = value

	def __add__(self, other):    # dodawanie macierzy
		if len(self.data) != len(other.data):
			raise ValueError
		m = Matrix(self.rows,self.cols)	
		for i in range(len(self.data)):	
			m.data[i] = self.data[i]+other.data[i]
		return m

	def __sub__(self, other):    # odejmowanie macierzy
		if len(self.data) != len(other.data):
			raise ValueError
		m = Matrix(self.rows,self.cols)	
		for i in range(len(self.data)):	
			m.data[i] = self.data[i]-other.data[i]
		return m

	def __mul__(self, other):    # mnożenie macierzy
		if isinstance(self, (int,float,long) ):
			newM = Matrix(0,0)
			newM.rows = other.rows
			newM.cols = other.cols
			newM.data = other.data
			for i in range(other.rows*other.cols):
				newM.data[i] = other.data[i] * self
			return newM
		elif isinstance(other, (int,float,long) ):
			newM = Matrix(0,0)
			newM.rows = self.rows
			newM.cols = self.cols
			newM.data = self.data
			for i in range(self.rows*self.cols):
				newM.data[i] = self.data[i] * other
			return newM
		elif self.cols == other.rows:
			newM = Matrix(self.cols,other.rows)
			for i in range(self.cols):
				for k in range(self.cols):
					for j in range(other.rows):
						newM[i,k] = newM[i,k] + self[i,j]*other[j,k] 
			return newM
		else :
			raise ValueError
			
# Zastosowanie.
m = Matrix(4, 4)

for i in range(4):
	for j in range(4):
		m[i,j] = i+1*j+1

  # metoda __setitem__
print m[1, 2]                 # metoda __getitem__
print m                       # metoda __str__

print m+m
print m-m

print m*m
print m*5