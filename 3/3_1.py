x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
# Poprawne

for i in "qwerty": if ord(i) < 100: print i
# Nie poprawne - "if ord(i) < 100:" powinno byc w nowej linijce
# przesuniete o 4 spacje


for i in "axby": print ord(i) if ord(i) < 100 else i
# Poprawne