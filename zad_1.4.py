wiek = int(input('Podaj swoj wiek: '))
ilosc_nocy = int(input('Podaj ile nocy spedzisz w hotelu'))
oplata = 200
if wiek < 18:
    oplata = 100
elif ilosc_nocy >= 2 and ilosc_nocy <=5:
    oplata = 180
elif ilosc_nocy >5:
    oplata = 150
if wiek>=65:
    oplata = oplata * 0.9

oplata_koncowa = oplata * ilosc_nocy
print(oplata_koncowa, 'PLN')