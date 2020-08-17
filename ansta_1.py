#!/usr/bin/env python3

'''
Michał Jabłonowski
Zadanie 1. do CV
'''


# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
def zad_1(first, last):
    # zmienne
    list = [first]
    code = ''
    
    # zmiana typów danych; string -> integer
    first = first.replace('-','')
    start = int(first)
    
    last = last.replace('-','')
    end = int(last)
    
    # inkrementacja kodu pocztowego & wpisanie poprawnego kodu do listy
    while start != end:
        start += 1
        code = str(start)
        code = code[:2] + '-' + code[2:]
        list.append(code)
        
    print(list)
    

if __name__ == '__main__':
    zad_1("79-900","80-155")

