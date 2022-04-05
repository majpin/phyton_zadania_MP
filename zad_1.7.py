towar = input('Podaj co chcesz dzis kupic: ')
ile = int(input('ile chcesz kupic?: '))
cena = int(input('ile kosztuje dany produkt?: '))
naleznosc = cena * ile
print(f'Do zaplaty jest {naleznosc} pln za {towar}')