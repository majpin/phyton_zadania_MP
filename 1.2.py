dni = {1: 'poniedzialek',2: 'wtorek', 3: 'sroda', 4: 'czwartek', 5: 'piatek', 6: 'sobota', 7: 'niedziela'}
print(dni)
dzien = int(input('Podaj dzien w ktorym buty zostaly oddane: '))
czas = int(input('Podaj czas naprawy: '))
termin = dzien + czas - ((dzien + czas) //7 ) * 7
print( f' dzien w ktorym mozesz odebrac buty to: {dni.get(termin)}')
# do powtorki ( nie rozumiem za bardzo)
