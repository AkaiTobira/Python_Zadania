
def make_measure(n):
	"""Funkcja tworzaca miarke o dlugosci n"""
	s = ""
	for i in range(n):
		s += "|...."
	s+= "|\n"

	for i in range(n+1):
		if i < 9 : 
			s+= str(i) + "    "
		else :
			s+= str(i) + "   "

	s = s[0:len(s)-3]
	return s

def make_net(n,k):
	"""Funkcja tworzaca siatke o wymiarach NxK"""
	output = ""
	for j in range(k):
		for i in range(n):
			output += "+---"
		output += "+\n"
		for i in range(n):
			output += "|   "
		output += "|\n"
	
	for i in range(n):
			output += "+---"
	output += "+"

	return output

print make_measure(12)

#|....|....|....|....|....|....|....|....|....|....|....|....|
#0    1    2    3    4    5    6    7    8    9   10   11   12

print make_net(7,4)

#+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+

