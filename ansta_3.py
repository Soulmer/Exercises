#!/usr/bin/env python3

'''
Michał Jabłonowski
Zadanie 3. do CV
'''


# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
def zad_3(start, end):
    # zmienna
    list = [float(start)]

    # generowanie liczb & zapisanie liczb do listy
    while float(start) < float(end):
        start += 0.5
        list.append(float(start))
    
    print(list)
    

if __name__ == '__main__':
    zad_3(2,5.5)

