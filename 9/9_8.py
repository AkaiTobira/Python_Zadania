#!/usr/bin/python
# -*- coding: utf-8 -*-
#


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:      # na prawo
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:    # na lewo
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass    # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return False


class BinarySearchTree:
    """Klasa reprezentująca binarne drzewo poszukiwań."""

    def __init__(self):
        self.root = None

    def __str__(self):
	return str(self.root.right.data)

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def count(self):
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return False


def bst_max(top): 
	if top == None:
		return ValueError
	temp = top
	while temp.right != None:
		temp = temp.right
	return temp.data
		

def bst_min(top): 
	if top == None:
		return ValueError
	temp = top
	while temp.left != None:
		temp = temp.left
	return temp.data

P = None
K = BinarySearchTree()
K.insert(3)
K.insert(1)
K.insert(-3)
K.insert(83)
K.insert(31)
K.insert(63)
K.insert(13)
K.insert(630)
K.insert(-63)
print K
print bst_max(K.root)
print bst_min(K.root)
print bst_min(P)