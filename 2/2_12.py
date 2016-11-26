
line = "Wplynolem na suchego przestwor oceanu\nWoz \t nurza sie w zielonosc i jak lodka brodzi\nSrod fali lak\t szumiacych, srod kwiatow powodzi\nOmijam \t koralowe ostrowy burzany"

print line

L = line.split("\n")
fowa = ""
back = ""

for item in L:
	fowa = fowa + item[0:1]

print fowa

for item in L:
	back = back + item[len(item)-1:len(item)]

print back
