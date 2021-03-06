#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import itertools


class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.size = n + 1       # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):   # poly1 + poly2
	
	if self.is_zero() and other.is_zero():
		return Poly(0,0)
	elif self.is_zero() :
		return other
	elif other.is_zero():
		return self
	L = [x+y for (x,y) in itertools.izip_longest(self.a, other.a, fillvalue=0 )]
	Pol = Poly()
	Pol.size = len(L)
	Pol.a = L
	return Pol
	

    def __sub__(self, other):   # poly1 - poly2
	if self.is_zero() and other.is_zero():
		return Poly(0,0)
	elif self.is_zero() :
		return other
	elif other.is_zero():
		return self
	
	L = [x-y for (x,y) in itertools.izip_longest(self.a, other.a, fillvalue=0 )]
	Pol = Poly()
	Pol.size = len(L)
	Pol.a = L
	return Pol


    def __mul__(self, other):  # poly1 * poly2
         L = [0]*(self.size+other.size-1)
         for i in range(self.size):
             for j in range(other.size):
                 L[i+j] = L[i+j] + self.a[i] * other.a[j]
	 K = Poly(0,self.size+other.size-2)
	 K.a = L
         return K

    def __pos__(self):          # +poly1 = (+1)*poly1
	return self

    def __neg__(self):          # -poly1 = (-1)*poly1
	L = [self.a[x]*-1 for x in range(self.size)]
	Pol = Poly()
	Pol.size = len(L)
	Pol.a = L
	return Pol

    def __eq__(self, other):    # obsługa poly1 == poly2
	if self.size != other.size :
		return False
	else:
		for i in range(self.size):
			if self.a[i] != other.a[i]:
				return False
	return True

    def __ne__(self, other):        # obsługa poly1 != poly2
        return not self == other

    def eval(self, x):         # schemat Hornera
	res = 0 
	for item in reversed(self.a):
		res = res*x+item
	return res
	

    def combine(self, other):     # złożenie poly1(poly2(x))
	R2 = Poly(0,0)
        for i in range(self.size):
            R1 = other	
            for j in range(i-1):
                R1 = R1 * other
            R2 = R2 + ( R1 * Poly(self.a[i],0) )
        
        return R2


    def __pow__(self, n):       # poly(x)**n lub pow(poly(x),n)
	G = self
	for i in range(n-1):
		G = G * self
	return G


    def diff(self):             # różniczkowanie
	L = [0]*(self.size-1)	
	for i in range(self.size-1):
		L[i] = self.a[i+1]*(i+1)
	K = Poly(len(L),0)
	K.size = len(L)
	K.a = L
	return K


    def integrate(self):        # całkowanie
	L = [0.0]*(self.size+1)
	for i in range(self.size):
		L[i+1] = float(self.a[i])/float((i+1))
	K = Poly(len(L),0)
	K.size = len(L)
	K.a = L
	return K

    def is_zero(self):          # bool, True dla [0], [0, 0],...
	for i in range(self.size):
		if self.a[i] != 0 :
			return False
	return True

# Kod testujący moduł.

import unittest

class TestPoly(unittest.TestCase): 

    def setUp(self): 
	self.one = Poly(5,5)
	self.one.a[4] = 3
	self.one.a[3] = 2
	self.one.a[2] = 1
	self.one.a[1] = 8
	self.two = Poly(4,4)
	self.two.a[2] = 2
	self.two.a[1] = 1
	self.two.a[0] = 8


    def test_print(self): 
	self.assertEquals( str(self.one), "[0, 8, 1, 2, 3, 5]")
	

    def test_add(self): 
	self.assertEquals( str(self.one + Poly(self.one.a[1],0)), "[8, 8, 1, 2, 3, 5]" )
	self.assertEquals( str(self.one + self.two) , "[8, 9, 3, 2, 7, 5]")
	self.assertEquals( str(self.two + self.one) , "[8, 9, 3, 2, 7, 5]")
	self.assertEquals( str(self.one + self.one) , "[0, 16, 2, 4, 6, 10]")

    def test_sub(self): 
	self.assertEquals( str(self.one - self.two) , "[-8, 7, -1, 2, -1, 5]")
	self.assertEquals( str(self.two - self.one) , "[8, -7, 1, -2, 1, -5]")
	self.assertEquals( str(self.one - self.one) , "[0, 0, 0, 0, 0, 0]")
	
    def test_mul(self):
	one = Poly(2,3)
	one.a[2] = 4
	one.a[1] = -1
	one.a[0] = -1
	two = Poly(1,4)
	two.a[1] = 1
	two.a[0] = 1
	self.assertEquals( str(two * Poly(1,1)), "[0, 1, 1, 0, 0, 1]") 
	self.assertEquals( str(self.one * Poly(self.one.a[1],0)), "[0, 64, 8, 16, 24, 40]" )
	self.assertEquals( str(one * two) , "[-1, -2, 3, 6, 1, -1, 4, 2]")

    def test_pos(self):
	self.assertEquals( str(+self.one), "[0, 8, 1, 2, 3, 5]")
	self.assertEquals( str(-self.one), "[0, -8, -1, -2, -3, -5]" ) 

    def test_eq(self):
	self.assertFalse( self.one == self.two )
	self.assertTrue( self.two == self.two )

    def test_eval(self):
	self.assertEquals( self.two.eval(4), 8+4+2*16+4*16*16 )

    def test_comb(self):
	one = Poly(2,2)
	one.a[1] = 3
	two = Poly(3,3)
	two.a[0] = 6
	self.assertEquals( str(one.combine(two)) , "[90, 0, 0, 81, 0, 0, 18]")

    def test_pow(self):
	two = Poly(3,3)
	two.a[0] = 6
	self.assertEquals( str(two**2), "[36, 0, 0, 36, 0, 0, 9]" )
	self.assertEquals( str(two**3), "[216, 0, 0, 324, 0, 0, 162, 0, 0, 27]" )
	self.assertEquals( str(two**9), str(two*two*two*two*two*two*two*two*two) )

    def test_diff(self):
	self.assertEquals(str(self.one.diff()),"[8, 2, 6, 12, 25]")

    def test_inf(self):
	one = Poly(25.0,4)
	one.a[3] = 12.0
	one.a[2] = 6.0
	one.a[1] = 2.0
	one.a[0] = 8.0
	
	self.assertEquals(str(one.integrate()), "[0.0, 8.0, 1.0, 2.0, 3.0, 5.0]")

    def test_zero(self):
	for i in range(100):
		one = Poly(0,i)
		self.assertTrue(one.is_zero())
	self.assertFalse(self.one.is_zero())

    def tearDown(self): pass



if __name__ == "__main__":
    unittest.main()     # wszystkie testy

