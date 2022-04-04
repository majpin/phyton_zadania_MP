wzrost = float(input('Podaj ile masz wzrostu w cm: '))
masa = float(input('Podaj swoja mase ciala w kg: '))

bmi = masa / (wzrost/100)**2
print('BMI: ')
if bmi < 18.5:
    print("Niedowaga")
elif 18.5 <= bmi < 25:
    print("W normie")
elif 25 <= bmi < 30:
    print("Nadwaga")
else:
    print("Otylosc")