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

    def __mul__(self, other): pass   # mnożenie macierzy

# Zastosowanie.
m = Matrix(3, 4)
m[1, 2] = 12                  # metoda __setitem__
print m[1, 2]                 # metoda __getitem__
print m                       # metoda __str__

print m+m
print m-m