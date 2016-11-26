line = "Wplynolem na suchego przestwor oceanu,\n Woz \t nurza sie w zielonosc i jak lodka brodzi,\n Srod fali lak\t szumiacych, srod kwiatow powodzi,\n Omijam \t koralowe ostrowy burzany."

print line

L = line.split("\n")
out = ""
" " 
for item in L :
	if item != "" :
		out = out + item + " "

L = out.split("\t")

out = ""

for item in L :
	if item != "" :
		out = out + item + " "

L = out.split(" ")
out = ""

for item in L :
	if item != "" :
		out = out + item + " "

L = out.split(" ")
del L[len(L)-1]
#algorym z 2_10

L.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))
print L

L.sort(cmp=lambda x,y: cmp(len(x),len(y)))
print L

