#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from math import sqrt

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x=0, y=0):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
	return "(" + str(self.x) + ", "+ str(self.y) + ")"

    def __repr__(self):         # zwraca string "Point(x, y)"
	return "Point" + str(self)

    def __eq__(self, other):    # obsługa point1 == point2
	return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):    # v1 + v2
	return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
	return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
	return Point(self.x * other.x, self.y * other.y)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
	return float(sqrt(self.x * self.x + self.y * self.y))
# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 

    def setUp(self): pass

    def test_print(self):       # test str() i repr()
	self.assertEqual( str(Point(1,2)) , "(1, 2)")
	self.assertEqual( repr(Point(1,2)) , "Point(1, 2)")

    def test_eq(self):
	self.assertTrue ( Point(12,5) == Point(12,5) )
	self.assertFalse( Point(12,5) == Point(1,5)  )

    def test_ne(self):
	self.assertTrue ( Point(12,5) != Point(1,5)  )
	self.assertFalse( Point(12,5) != Point(12,5) )

    def test_sub(self):
        self.assertEqual(Point(1,2) + Point(4,1), Point(5,3))

    def test_add(self):
        self.assertEqual(Point(1,2) - Point(4,1), Point(-3,1))

    def test_mul(self):
        self.assertEqual(Point(2,2) * Point(4,3), Point(8,6))

    def test_length(self): 
	self.assertEqual(Point(4,3).length(), 5)  
	self.assertAlmostEqual(Point(9,3).length(), 9.48683298, places=6, msg=None)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy
