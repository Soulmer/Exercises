#!/usr/bin/env python3

'''
Michał Jabłonowski
Zadanie 2. do CV
'''


# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
def zad_2(list_check, n):
    # zmienne
    list = []
    for i in range (n):
        list.append(i+1)
        
    list_result = []
    
    # sprawdzenie jakich elementów brakuje w liście & zapisanie brakujących elementów do list_result
    for i in range (len(list)):
        if list[i] in list_check:
            continue
        else:
            list_result.append(list[i])
            
    print(list_result)
    

if __name__ == '__main__':
    zad_2([2,3,7,4,9],10)

