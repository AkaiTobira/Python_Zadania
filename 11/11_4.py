#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from random import gauss
from random import shuffle
import time

def randomNoSort( l ):
	L = []
	for i in range(l):
		L.append(i)
	shuffle(L)
	return L

def swap(L,i,j):
	temp = L[i]
	L[i] = L[j]
	L[j] = temp
	del temp
	
def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
		swap(L,i,k)


def insertsort(L, left, right):
    for i in range(right, left, -1):   # ustawiam wartownika
        if L[i-1] > L[i]: 
            swap(L, i-1, i)
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:   # robimy miejsce na item
            L[j] = L[j-1]
            j = j-1
        L[j] = item

def bubblesort(L, left, right):
    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j+1]:
                swap(L, j+1, j)

def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k

def shellsort(L, left, right):
    # Ustalenie największego kroku z sekwencji:
    # 1, 4, 13, 40, 121, 364, 1093, 3280, 9841, ...
    h = 1
    while h <= (right-left) / 9:
        h = 3*h+1
    while h > 0:
        for i in range(left+h, right+1):
            j = i
            # Zamiast swap() mamy przesuniecia.
            item = L[i]
            while j >= left+h and item < L[j-h]:
                L[j] = L[j-h]
                j = j-h
            L[j] = item
        h = h / 3


def quicksort(L, left, right):
    """Sortowanie szybkie wg Cormena str. 169."""
    if left >= right:
        return
    pivot = partition(L, left, right)
    # pivot jest na swoim miejscu.
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def partition(L, left, right):
    """Zwraca indeks elementu rozdzielającego."""
    # Element rozdzielający to ostatni z prawej,
    # dlatego na końcu trzeba go przerzucić do środka.
    # Będzie on na docelowej pozycji ze względu na sortowanie.
    x = L[right]   # element rozdzielający
    i = left
    for j in range(left, right):
        if L[j] <= x:
            swap(L, i, j)
            i = i + 1
    swap(L, i, right)
    return i

def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) / 2   # wyznaczanie środka 
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie
    
def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji z wartownikami."""
    n1 = middle - left + 1
    n2 = right - middle
    A = [None] * (n1 + 1)
    B = [None] * (n2 + 1)
    for i in range(n1):
        A[i] = L[left + i]
    for i in range(n2):
        B[i] = L[middle + 1 + i]
    A[n1] = float("inf")   # wartownik
    B[n2] = float("inf")   # wartownik
    i, j = 0, 0
    for k in range(left, right+1):
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1

outfile = open("output","w")
T = []
for j in range(5):
	L = []
	G = []
	for i in range(7):
		L.append(randomNoSort(10**(j+2)))

	A_start = time.time()
	selectsort(L[1],0,len(L[1])-1)
	A_stop = time.time()
	G.append("SelectSort: " + str(A_stop - A_start))
	
	print "SS DONE"
	
	A_start = time.time()
	insertsort(L[0],0,len(L[0])-1)
	A_stop = time.time()
	G.append("InsertSort: " + str(A_stop - A_start))
	
	print "IS DONE"
	
	A_start = time.time()
	bubblesort(L[2],0,len(L[2])-1)
	A_stop = time.time()
	G.append("BubbleSort: " + str(A_stop - A_start))
	
	print "BS DONE"
	
	A_start = time.time()
	shakersort(L[3],0,len(L[3])-1)
	A_stop = time.time()
	G.append("ShekerSort: " + str(A_stop - A_start))
	
	print "ShrS DONE"
	
	A_start = time.time()
	shellsort(L[4],0,len(L[4])-1)
	A_stop = time.time()
	G.append("ShellSort: " + str(A_stop - A_start))
	
	print "SheS DONE"
	
	A_start = time.time()
	quicksort(L[5],0,len(L[5])-1)
	A_stop = time.time()
	G.append("QuickSort: " + str(A_stop - A_start))
	
	print "QS DONE"
	
	A_start = time.time()
	mergesort(L[6],0,len(L[6])-1)
	A_stop = time.time()
	G.append("MergeSort: " + str(A_stop - A_start))
	
	T.append(G)
	print "MS DONE"
	
	print j


outfile.write(str(T))
outfile.close()
            
            