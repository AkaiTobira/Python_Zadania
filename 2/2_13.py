line = "wplynolem na suchego przestwor oceanu,\n Woz \t nurza sie w zielonosc i jak lodka brodzi,\n Srod fali lak\t szumiacych, srod kwiatow powodzi,\n Omijam \t koralowe ostrowy burzany."

print line

L = line.split()

couter = 0
for item in L:
	couter+=len(item)

print couter  
