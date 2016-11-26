
L = L.sort() 
# (?) Nie wiemy co jest w liscie wiec jesli nie sortujemy napisow to
# dostaniemy pusta tablice.

x, y = 1, 2, 3 
# przypisanie zbyt wielu wartosci do zamalej liczby zmiennych 

X = 1, 2, 3; X[1] = 4 
# Krotki sa jak lancuchy znakow i nie mozna ich modyfikowac czesciowo   

X = [1, 2, 3] ; X[3] = 4 
# numerowanie indeksow zaczyna sie od 0 wiec 3 indeks jest poza lista

X = "abc" ; X.append("d") 
# "str" nie posiada metody append()

map(pow, range(8)) 
# funkcja pow() nie otrzymala argumentow