
#Ponizszy kod wypisze qwerty, poniewaz X jest zmienna globalna
X = "qwerty"

def func():
    print X

func()

#Ponizszy kod wypisze najpierw abc a potem qwerty, poniewaz X jest zmienna globalna "Print X" napisze qwerty, a funkcja func posiada niezalezna zmienna lokalna X

X = "qwerty"

def func():
    X = "abc"

func()
print X

#Ponizszy kod zamieni wartosc zmiennej globalnej X z "qwerty" na "abc"  

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print X
