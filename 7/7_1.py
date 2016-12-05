#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from fractions import gcd  

class Frac:
    """Klasa reprezentująca ułamki."""
    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
	"""Funkcja inicjująca"""
        self.x = x
        self.y = y

    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
	"""Funkcja konwertujaca na string"""
	if self.y == 1 :
	    return str(self.x)
	else:
	    return str(self.x) + "/" + str(self.y)
  
    def __repr__(self):         # zwraca "Frac(x, y)"
	return "Frac(" + str(self.x) + ", " + str(self.y) + ")"
	
    def __add__(self, other):      # frac1+frac2, frac+int
	if isinstance(other,(int,long,float)):
	    return self + Frac(other,1)
	frac = Frac(self.x * other.y + self.y * other.x, self.y*other.y )	
	return frac.__correct()


    def __radd__(self, other):
        return self.__add__(other)              # int+frac

    def __sub__(self, other):         # frac1-frac2, frac-int
	if isinstance( other, (int,float,long)):
		return Frac(self.y * other -  self.x,  self.y)
	if isinstance( self, (int,float,long)):
		return Frac(other.y * self - other.x , other.y)
	frac = Frac(self.x * other.y - self.y * other.x, self.y*other.y )
	return frac.__correct()

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
	if isinstance( other, (int,float,long)):
		return Frac(self.x - self.y * other, self.y)
	if isinstance( self, (int,float,long)):
		return Frac(other.x - other.y * self, other.y)
        return other-self

    def __correct(self):
	if self.x == 0 :
	    return Frac()
	
	temp = gcd(self.x,self.y)

	if temp	 != 1:
	    self.x = self.x/temp
	    self.y = self.y/temp

	if self.x > 0 and self.y < 0:
	    self.x = self.x*-1
	    self.y = self.y*-1

	if self.x < 0 and self.y < 0:
	    self.x = self.x*-1
	    self.y = self.y*-1

	return self
	

    def __mul__(self, other):         # frac1 * frac2
	if isinstance(self,(int,float,long)):
		return Frac( other.x * self, other.y).__correct()
	if isinstance(other,(int,float,long)):
		return Frac( other * self.x, self.y).__correct()

	frac = Frac(self.x * other.x, self.y*other.y )
	return frac.__correct()	

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):         # frac1/frac2, frac/int
		
	if isinstance(self, (int,float,long)):
		return Frac(self,1)/other
	if isinstance(other, (int,float,long)):
		if other == 0:
			raise ZeroDivisionError
		return self/Frac(other,1)
	if other.x == 0:
	    raise ZeroDivisionError
	frac = Frac(self.x * other.y, other.x*self.y )
		
	return frac.__correct()

    def __rdiv__(self,other):
	if isinstance(self, (int,float,long)):
		if self == 0:
			raise ZeroDivisionError
		return other/Frac(self,1)
	if isinstance(other, (int,float,long)):
		return Frac(other,1)/self
 
	    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
	return self

    def __neg__(self):          # -frac = (-1)*frac
	return self * -1

    def __invert__(self):       # odwrotnosc: ~frac	
	return Frac(self.y,self.x).__correct()

    def is_positive(self):              # bool, czy dodatni
	return (self.x > 0 and self.y > 0) or (self.x < 0 and self.y < 0)  

    def is_zero(self):                  # bool, typu [0, x]
	return self.x == 0 

    def __cmp__(self, other):         # -1 | 0 | +1
	if float(self) > float(other):
		return 1
	elif float(self) == float(other):
		return 0
	else :
		return -1


    def __float__(self): 
	if self.y == 0 :
	     raise ZeroDivisionError
	return float(self.x)/float(self.y)              # konwersja do float


import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = Frac(0, 1)

    def test_str(self):
	self.assertEqual(str(Frac(3,8)), "3/8")
	self.assertEqual(str(Frac(3,1)), "3")
	self.assertEqual(repr(Frac(3,8)), "Frac(3, 8)")

    def test_add_frac(self):
        self.assertEqual(Frac(1,2) + Frac(1,3), Frac(5, 6))
	self.assertEqual(Frac(1,6) + Frac(3, 2) + Frac(4, 3), Frac(3, 1))
	self.assertEqual(Frac(3,5) + Frac(-4,5), Frac(-1,5))
	self.assertEqual(Frac(-1,7) + Frac(1,7), self.zero)
	self.assertEqual(Frac(4,5) + 2 , Frac(14,5))
	T = Frac()	
	T = 2 + Frac(4,5)
	self.assertEqual( T , Frac(14,5))


    def test_sub_frac(self): 
	self.assertEqual(Frac(1,2) - Frac(1,3),  Frac(1, 6))
	self.assertEqual(Frac(3,5) - Frac(-4,5), Frac(7,5))
	self.assertEqual(Frac(1,6) - ( Frac(-1, 2) -  Frac(1,-3) ), Frac(1, 3))
	self.assertEqual(Frac(-1,7) - Frac(-1,7), self.zero)
	self.assertEqual(Frac(12,3) - 4 , self.zero)
	self.assertEqual( 4 - Frac(12,3) , self.zero)

    def test_mul_frac(self): 
	self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))
	self.assertEqual(Frac(3,5)  * Frac(-4,5), Frac(-12,25))
	self.assertEqual(Frac(3,1) * Frac(1, 2) * Frac(2,3), Frac(1, 1))
	self.assertEqual(Frac(-2,2) * Frac(3,-1), Frac(3,1))
	self.assertEqual(Frac(-4,2) * -1 , Frac(2,1))
	self.assertEqual( -1 * Frac(-4,2), Frac(2,1))

    def test_div_frac(self): 
	self.assertEqual(Frac(1, 2)/Frac(1, 3), Frac(3, 2))
	self.assertEqual(Frac(3, 5)/Frac(-4,5), Frac(-3,4))
	self.assertEqual(Frac(3, 1)/(Frac(1, 2)/Frac(2,3)), Frac(4, 1))
	self.assertEqual(Frac(-2,2)/Frac(3,-1), Frac(1,3))
	self.assertRaises(ZeroDivisionError, Frac.__div__, Frac(-2,6),Frac(0,1))
	self.assertEqual(Frac(2,3)/2, Frac(1,3))
	self.assertEqual(4/Frac(2,3), Frac(6,1))
	

    def test_pos(self):
	self.assertEqual( +Frac(4,9), Frac(4,9) )
	self.assertEqual( -Frac(4,9), Frac(-4,9) )

    def test_inve(self):
	self.assertEqual( ~Frac(4,9), Frac(9,4) )

    def test_is_positive(self):
	self.assertTrue(Frac(2,3).is_positive())
	self.assertFalse(Frac(2,-3).is_positive())
	self.assertFalse(Frac(-2,3).is_positive())
	self.assertTrue(Frac(-2,-3).is_positive())

    def test_is_zero(self): 
	self.assertEqual(Frac(0,2).is_zero(),True)
	self.assertEqual(Frac(6,2).is_zero(),False)

    def test_cmp_frac(self): 
	self.assertFalse(Frac(1, 3) > Frac(1, 2))
	self.assertFalse(Frac(1, 2) > Frac(1, 2))
	self.assertTrue(Frac(1, 2) > Frac(1, 3))
	


    def test_float(self): 
	self.assertAlmostEqual(float(Frac(1,3)), 0.33333333, places=7, msg=None)
	self.assertAlmostEqual(float(Frac(1,2)), 0.5, places=7, msg=None)
	self.assertRaises(ZeroDivisionError, Frac.__float__, Frac(2,0))	

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

