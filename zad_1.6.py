wiek = int(input('Podaj swoj wiek: '))
ilosc = int(input('Podaj ile biletow chcesz kupic?: '))

if 0 <= wiek <= 6:
    cena = 0
elif 7 <= wiek <=17:
    cena = 2.28
elif 18 <= wiek >= 64:
    cena = 3.80
else:
    cena = 1.90

naleznosc = ilosc * cena
print (f'do zaplacenia jest: {naleznosc}zl za {ilosc} biletow')

