from fractions import gcd  

def add_frac(frac1, frac2):      # frac1 + frac2
	frac = list()	
	frac.append(frac1[0]*frac2[1] + frac1[1]*frac2[0])
	frac.append(frac1[1]*frac2[1])

	if frac[0] == 0 :
		return [0,1]
	temp = gcd(frac[0],frac[1])

	if temp	 != 1:
		frac[0] = frac[0]/temp
		frac[1] = frac[1]/temp

	if frac[0] > 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1

	if frac[0] < 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1

	return frac

def sub_frac(frac1, frac2):         # frac1 - frac2
	frac = list()	
	frac.append(frac1[0]*frac2[1] - frac1[1]*frac2[0])
	frac.append(frac1[1]*frac2[1])
	if frac[0] == 0 :
		return [0,1]
	temp = gcd(frac[0],frac[1])

	if temp	 != 1:
		frac[0] = frac[0]/temp
		frac[1] = frac[1]/temp

	if frac[0] > 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1

	if frac[0] < 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1
	return frac

def mul_frac(frac1, frac2):         # frac1 * frac2
	frac = list()	
	frac.append(frac1[0]*frac2[0])
	frac.append(frac1[1]*frac2[1])
	if frac[0] == 0 :
		return [0,1]
	temp = gcd(frac[0],frac[1])
	if temp	 != 1:
		frac[0] = frac[0]/temp
		frac[1] = frac[1]/temp

	if frac[0] > 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1

	if frac[0] < 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1
	return frac	

def div_frac(frac1, frac2):        # frac1 / frac2
	frac = list()
	if frac2[0] == 0:
		raise ZeroDivisionError	
	frac.append(frac1[0]*frac2[1])
	frac.append(frac1[1]*frac2[0])
	if frac[0] == 0 :
		return [0,1]
	temp = gcd(frac[0],frac[1])

	if temp	 != 1:

		frac[0] = frac[0]/temp
		frac[1] = frac[1]/temp

	if frac[0] > 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1

	if frac[0] < 0 and frac[1] < 0:
		frac[0] = frac[0]*-1
		frac[1] = frac[1]*-1

	return frac


def is_positive(frac):              # bool, czy dodatni
	return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)  

def is_zero(frac):                  # bool, typu [0, x]
	return frac[0] == 0 

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
	if frac2float(frac1) > frac2float(frac2):
		return 1
	elif frac2float(frac1) == frac2float(frac2):
		return 0
	else :
		return -1


def frac2float(frac): 
	if frac[1] == 0 :
		raise ZeroDivisionError
	return float(frac[0])/float(frac[1])              # konwersja do float

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
	self.assertEqual(add_frac([1,6],add_frac([3, 2], [4, 3])), [3, 1])
	self.assertEqual(add_frac([3,5],[-4,5]),[-1,5])
	self.assertEqual(add_frac([-1,7],[1,7]),self.zero)

    def test_sub_frac(self): 
	self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
	self.assertEqual(sub_frac([3,5],[-4,5]),[7,5])
	self.assertEqual(sub_frac([1,6],sub_frac([-1, 2], [1,-3])), [1, 3])
	self.assertEqual(sub_frac([-1,7],[-1,7]),self.zero)

    def test_mul_frac(self): 
	self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
	self.assertEqual(mul_frac([3,5],[-4,5]),[-12,25])
	self.assertEqual(mul_frac([3,1],mul_frac([1, 2], [2,3])), [1, 1])
	self.assertEqual(mul_frac([-2,2],[3,-1]), [3,1])

    def test_div_frac(self): 
	self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
	self.assertEqual(div_frac([3,5],[-4,5]),[-3,4])
	self.assertEqual(div_frac([3,1],div_frac([1, 2], [2,3])), [4, 1])
	self.assertEqual(div_frac([-2,2],[3,-1]), [1,3])
	self.assertRaises(ZeroDivisionError, div_frac, [-2,6],[0,1])

    def test_is_positive(self):
	self.assertTrue(is_positive([2,3]))
	self.assertFalse(is_positive([2,-3]))
	self.assertFalse(is_positive([-2,3]))
	self.assertTrue(is_positive([-2,-3]))

    def test_is_zero(self): 
	self.assertEqual(is_zero([0,2]),True)
	self.assertEqual(is_zero([23,6]),False)

    def test_cmp_frac(self): 
	self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
	self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
	self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)


    def test_frac2float(self): 
	self.assertAlmostEqual(frac2float([1,3]), 0.33333333, places=7, msg=None)
	self.assertAlmostEqual(frac2float([1,2]), 0.5, places=7, msg=None)
	self.assertRaises(ZeroDivisionError, frac2float, [-2,0])	

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

