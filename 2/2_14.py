line = "wplynolem na suchego przestwor oceanu\n Woz \t nurza sie w zielonosc i jak lodka brodzi\n Srod fali lak\t szumiacych srod kwiatow powodzi\n Omijam \t koralowe ostrowy burzany"

print line

L = line.split()

smallest = ""
number   = 0
for item in L:
	if len(item) > number:
		number = len(item)
		smallest = item

print smallest, number

	
