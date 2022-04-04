z = int(input('Ile kosztuje kilo ziemniakow?: '))
zk = int(input('Ile chcesz kilo ziemniakow kupic?'))
b = int(input ('Ile kosztuje kilo bananow?: '))
bk = int(input('Ile kilo bananow chcesz kupic?: '))
naleznosc = z * zk
naleznosc_2 = b * bk
naleznosc_3 = (z * zk ) + (b * bk)
if z > b:
    print('Ziemniaki kosztuja wiecej')
else:
    print('Banany kosztuja wiecej')


print(f'Naleznosc', {naleznosc}, {naleznosc_2}, {naleznosc_3},'PLN' )